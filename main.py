
import pandas as pd
import json
import csv

# Abre el archivo GeoJSON y carga los datos
with open('archivo.geojson', 'r') as f:
    data = json.load(f)

# Extrae los datos de las características y conviértelos en una lista de diccionarios
    features = data['features']
    dict_list = []
    for feature in features:
        properties = feature['properties']
        coordinates = feature['geometry']['coordinates']
        record = {'id': properties['id'], 'title': properties['title'], 'annual_visits': properties['annual_visits'],
                  'longitude': coordinates[0], 'latitude': coordinates[1]}
        dict_list.append(record)

# Escribe la lista de diccionarios a un archivo CSV
    with open('archivo.csv', 'w', newline='') as f:
        writer = csv.DictWriter(
            f, fieldnames=['id', 'title', 'annual_visits', 'longitude', 'latitude'])
        writer.writeheader()
        writer.writerows(dict_list)
