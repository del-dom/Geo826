# class10_homework.py
#
# The goal is to produce a map of the North American tropics
# with hurricane points from a database table overlain on it.
# The map is in Mercator, not nasty lat-lon. Wow, accomplish 
# this and you've programmed a GIS, haven't you?
# 
# This will take a couple of steps:
# 1. (not python) Load the hurricane sql dump file into your 
# database. It is a table called cane with lat, lon, and other  
# information about each North Atlantic hurricane from 1950-2002. 
# 
# 2. (python) Load the data from the database into a 
# multipoint Geometry object.
# 
# 3. Project each point coordinate to Mercator.
#
# 4. Plot a map of all projected hurricane points, in red or 
# blue, over a reference map of the coastal and national 
# boundary dataset as a backdrop.
#
# 5. Make a better map. Load a selection of hurricanes with 
#     low pressure, another selection with higher pressure,
#     and another with the highest pressure. Plot each group
#     using different symbol sizes and colors. Low pressure
#     means the hurricane is stronger!
#
# Hints: 
# 1. Read the Postgresql Tip Sheet.
# 2. Use drawCoast.py as a place to start.
# 3. You'll need to write a function to convert the lat/lon 
#    values to Mercator so that they match the coast data.
# 4. If you've lost your Mercator function, check wikipedia for 
#     the algorithm. Trig and log functions are in the math module. 
#     Trig functions assume radians, not decimal degrees - convert 
#     by multiplying degrees by pi/180
# 5. Are the longitude values in the db really correct? Or 
#    will you need to modify them in some way?
# 6. Turn the hurricane data into point class objects in 
#    Geometry for drawing.
#
# Due next Friday before class.

