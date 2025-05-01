import csv
import json

with open('atp_tennis.csv', newline='', encoding='latin1') as csvF:
    reader = csv.DictReader(csvF)
    data = list(reader)

bulk_data = {"docs": data}

with open('atp_tennis.json', 'w', encoding='utf-8') as jF:
    json.dump(bulk_data, jF, indent=4, ensure_ascii=False)
