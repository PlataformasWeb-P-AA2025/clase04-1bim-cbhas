import requests
import json

with open('atp_tennis.json', 'r') as f:
    data = json.load(f)

lista_datos = []

for d in data['docs']:
    lista_datos.append(d)

base_datos = "ejercicio001"

url = f"http://127.0.0.1:5984/{base_datos}/_bulk_docs"
headers = {'Content-Type': 'application/json'}

datos_finales = {'docs': lista_datos}
response = requests.post(url, headers=headers, json=datos_finales)

print(response.status_code)
print(response.json())
