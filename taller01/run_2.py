import requests
import json

with open('atp_tennis.json', 'r') as f:
    data = json.load(f)

lista_datos = []

for d in data['docs']:
    lista_datos.append(d)

base_datos = "ejercicio002"

url = f"http://127.0.0.1:5984/{base_datos}"
headers = {'Content-Type': 'application/json'}

for doc in lista_datos:
    response = requests.post(
        url,
        json=doc
    )
