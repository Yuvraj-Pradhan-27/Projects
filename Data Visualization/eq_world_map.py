from pathlib import Path
import json
import plotly.express as px

#Read data as a string and convert to a Python Object
path = Path('eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

#Examine all earthquakes in the dataset
all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
print(len(all_eq_dicts))

mags, lons, lats, eq_titles= [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color_continuous_scale='Viridis',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     )
fig.show()

# print(mags[:10])
# print(lons[:5])
# print(lats[:5])