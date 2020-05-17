# -*- coding: utf-8 -*-
"""
VUCC Circle Location Checker
Tony Milluzzi, KD8RTT 

This script checks all listed locations against one another
to determine if any are more than 200km apart. If any two locations
are more than 200km apart, a message will provide the details.
If all locations are less than or equal to 200km from one another,
a confirmation message will be printed.

For VUCC details, see rule 6:
https://www.arrl.org/files/file/Awards%20Application%20Forms/VUCCRULE1a.pdf
"""
from geopy import distance

# Enter a location name, latitude, and longitude (in degrees)
# for each location of interest. Add lines following the same
# format as desired.
locations = [['EM28OX', 38.978333, -94.793333],
             ['EM38CX_EM39CA', 38.999148, -93.787497],
             ['EM29PA', 39.020796, -94.74382],
             ['EM19XB', 39.044804, -96.039385],
             ['EM28MP', 38.658138, -94.921205],
             ['EM28IO', 38.597833, -95.270631]]

out = []
k = 0
count = 0

for i in range(len(locations)):
    for j in range(1,len(locations)):
        loc1 = locations[i][0]
        lat1 = locations[i][1]
        long1 = locations [i][2]
        loc2 = locations[i-j][0]
        lat2 = locations[i-j][1]
        long2 = locations[i-j][2]
        dist_km = distance.geodesic([lat1, long1], [lat2, long2]).km
        dist_mi = distance.geodesic([lat1, long1], [lat2, long2]).mi
        out.append([loc1, loc2, dist_km])
        
while k < len(out):
    loc1n = out[k][0]
    loc2n = out[k][1]
    dist = out[k][2]
    index = out.index([loc2n, loc1n, dist])
    del out[index]
    k=k+1
    if dist >= 200:
        print('Distance between ' + loc1n + ' and ' + loc2n + ' is ' + str(dist) + 'km')
    	count = count + 1
if count == 0:
	print('All locations are within 200km of one another.')       