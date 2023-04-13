import csv, json
import geojson



# Abre el archivo CSV y carga los datos
with open('archivo.csv', 'r') as f:
    reader = csv.DictReader(f)
    dict_list = [row for row in reader]

# Convierte la lista de diccionarios a un objeto FeatureCollection de GeoJSON
features = []
for record in dict_list:
    point = geojson.Point((float(record['longitude']), float(record['latitude'])))
    del record['longitude']
    del record['latitude']
    feature = geojson.Feature(geometry=point, properties=record)
    features.append(feature)
feature_collection = geojson.FeatureCollection(features)

# Escribe el objeto FeatureCollection a un archivo GeoJSON
with open('datos.geojson', 'w') as f:
    #geojson.dump(feature_collection, f)
    f.write(geojson.dumps(feature_collection))