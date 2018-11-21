import pandas
import folium

#print(dir(folium))


data = pandas.read_csv("WorldVolcanoes.txt")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
elev = list(data["Elevation"])

def colour_producer(elevation):
    if elevation > 3000:
        return 'red'
    elif elevation > 1000:
        return 'orange'
    else:
        return 'green'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=str(el) + " m", icon=folium.Icon(color=colour_producer(el))))
    #fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el) + " m", fill_color=colour_producer(el), color='grey', fill_opacity=0.7))

#adding a geojson polygon layer: choropleth with colour
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else ('orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red')}))


#feature groups for layer control
map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())
map.save("Map1.html")

