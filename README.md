# vucc_circle_check

This script checks a list of locations against one another to check if any are more than 200 km apart to meet the ARRL's VUCC rules. For more details, see https://kd8rtt.com/2020/05/17/vucc-circle-checker-script/

Using the script is fairly simple: just update the placeholder name for each location in the list and the associated latitude and longitude, and run the program from a terminal. Keep in mind the script expects latitude and longitude in decimal degrees format. If all locations are 200 km apart or less, a message will be printed that confirms this. Otherwise, the specific locations beyond the 200 km distance will be called out. As your list of locations grows, simply follow the same format and add additional lines to the "locations" list. Also, note that this script utilizes GeoPy, so be sure to install it beforehand (in addition to Python itself, of course). GeoPy uses the Karney algorithm for computing the geodesic distance.
