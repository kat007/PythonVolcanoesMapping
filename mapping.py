#pip install folium

import folium

#folium.map.legacymap

map = folium.Map(location=[-37,174], zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[-37,175], popup="Auckland", icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("Map1.html")
