# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 17:27:56 2017

@author: Thinky
"""

map_1 = folium.Map(location=[42.3736, -71.1097], zoom_start=12, tiles='Stamen Terrain')
folium.Marker([42.3601, -71.0942], popup='Tagged!').add_to(map_1)
folium.Marker([42.3641, -72.1942], popup='Tagged!').add_to(map_1)
folium.Marker([42.3651, -71.1342], popup='Tagged!').add_to(map_1)
folium.Marker([42.3741, -71.1362], popup='Tagged!').add_to(map_1)
folium.Marker([42.4641, -71.1842], popup='Tagged!').add_to(map_1)
map_1.save('mthood.html')
