import pandas as pd


import pandas as pd
df = pd.read_json (r'archivo.geojson')
df.to_csv (r'test.csv', index = None)