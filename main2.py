import pandas as pd
import json

# Abre el archivo GeoJSON y carga los datos
with open('archivo.geojson', 'r') as f:
    data = json.load(f)

# Extrae los datos de las características y conviértelos en un DataFrame de pandas
features = data['features']
df = pd.json_normalize(features)

# Elimina la columna geometry del DataFrame
#df = df.drop(columns='geometry')

# Escribe el DataFrame a un archivo CSV
df.to_csv (r'test1.csv', index = False)