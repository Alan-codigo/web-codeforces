import requests
from bs4 import BeautifulSoup

# Dirección de la página web de donde queremos extraer contenido
url = 'https://codeforces.com/contests/page/1'

# Realizamos la petición a la página web
response = requests.get(url)

# Comprobamos que la petición se haya realizado correctamente
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Encuentra todos los elementos 'tr' que tienen un 'data-contestid'.
    tr_elements = soup.find_all('tr', {'data-contestid': True})

    # Para cada 'tr', extraemos todos los 'td', su contenido y los enlaces.
    contests = []
    for tr in tr_elements:
        # Diccionario para almacenar la información del concurso
        contest_info = {'data': [], 'links': []}

        # Encuentra todos los elementos 'td' dentro de este 'tr' y obtén su texto.
        tds = tr.find_all('td')
        contest_info['data'] = [td.get_text(strip=True) for td in tds]

        # Encuentra todos los enlaces dentro de cada 'td' y obtén su atributo 'href'.
        links = tr.find_all('a')
        contest_info['links'] = [link.get('href') for link in links]

        # Agregar la información del concurso a la lista de concursos
        contests.append(contest_info)
else:
    contests = [f"Error al realizar la petición HTTP: {response.status_code}"]

# Imprimir los resultados
for contest in contests:
    print(contest)
