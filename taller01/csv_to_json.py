import csv
import json

with open('atp_tennis.csv', newline='', encoding='latin1') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

bulk_data = {"docs": data}

with open('atp_tennis.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(bulk_data, jsonfile, indent=4, ensure_ascii=False)
