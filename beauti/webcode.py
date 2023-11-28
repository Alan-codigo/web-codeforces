import requests
from bs4 import BeautifulSoup
import json
import os

contests = []

# Iteramos sobre las páginas desde la 1 hasta la 18.
for i in range(1, 19):
    url = f'https://codeforces.com/contests/page/{i}'
    
    # Realizamos la petición a la página web
    response = requests.get(url)

    # Comprobamos que la petición se haya realizado correctamente
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Encuentra todos los elementos 'tr' que tienen un 'data-contestid'.
        tr_elements = soup.find_all('tr', {'data-contestid': True})

        # Para cada 'tr', extraemos todos los 'td', su contenido y los enlaces.
        for tr in tr_elements:
            contest_info = {
                'data': [],
                'links': []
            }

            # Encuentra todos los elementos 'td' dentro de este 'tr' y obtén su texto.
            tds = tr.find_all('td')
            contest_info['data'] = [td.get_text(strip=True) for td in tds]

            # Encuentra todos los enlaces dentro de este 'tr' y obtén su atributo 'href'.
            links = tr.find_all('a')
            contest_info['links'] = [link.get('href') for link in links if link.get('href')]

            # Agregar la información del concurso a la lista de concursos
            contests.append(contest_info)
    else:
        print(f"Error al realizar la petición HTTP en la página {i}: {response.status_code}")

    print(i)

# Imprimir los resultados
for contest in contests:
    print(contest)


directory = 'C:/Users/alan_/OneDrive/Escritorio/webcrawler/beauti/'
file_name = 'contests.json'
file_path = os.path.join(directory, file_name)

# Crea el directorio si no existe
os.makedirs(directory, exist_ok=True)

# Abre el archivo para escribir, creando el archivo si no existe
with open(file_path, 'w', encoding='utf-8') as file:
    # Escribe la lista de concursos en el archivo en formato JSON
    json.dump(contests, file, ensure_ascii=False, indent=4)

print(f"Datos guardados en {file_path}")