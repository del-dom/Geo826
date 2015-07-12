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
done
# 
# 2. (python) Load the data from the database into a 
# multipoint Geometry object.
import psycopg2
import geometry
import geometrywk7
dbc = psycopg2.connect(database="geo826dd",  user="geo826dd", password="saS7ADap")
cursor = dbc.cursor()
cursor.execute("SELECT * FROM cane")
result = cursor.fetchall()
hurricanes = geometrywk7.MultiPoint(result)

# 3. Project each point coordinate to Mercator.
import math
hurricanes.points

''' function below converts lat/lon to x/y'''

def merc(lat,lon):
  import math
  if lat>89.9:lat=89.9 #makes sure that the latitude is a legal latitude
  if lat<-89.9:lat=-89.9
  R = 6378137 #earths radius
  phi = math.radians(lat)
  lon2 = lon * math.pi/180 #convert to radians. Could use math.radians for this like above.
  ts = math.tan((math.pi/4) + (phi/2))
  y = R * math.log(ts)
  x = (R * lon2)*-1
  return  x, y
   
''' the function below takes a geometry point class. It extracts the location data, converters from tuples to lists. Converters from lat/lon to x/y.
converts x/y to discrete point location.'''

def converter(points): # takes a geometry point class
    canes = []    
    step = []
    canesmercator = []
    for i in points.points:
	step = []
	for j in i:
	    #print type(j)
	    step.append(j)
	canes.append(step)
    for j in canes:
	canesmercator.append(merc(j[8], j[9]))
    for x,y in zip(canes,canesmercator):
	x.append(y)
    Lmerc = []
    step2 =[]
    for i in canesmercator:
	step2=[]
	for j in i:
	    step2.append(j)
	Lmerc.append(step2)
    plistnew = []
    for i in Lmerc:
	plistnew.append(geometry.Point(i[0],i[1]))
    return plistnew

pointlist = converter(hurricanes)
    
# 4. Plot a map of all projected hurricane points, in red or 
# blue, over a reference map of the coastal and national 
# boundary dataset as a backdrop.
import drawCoast
import GISgraphics

All = geometry.MultiPoint(pointlist)
mapwin2 = GISgraphics.MapWindow(': Hurricanes', winXY=(600,400),\
mapSize=All.envelope)
coasts.draw(mapwin2, 'white', 1)
a = raw_input('Hit Enter to Quit ')



# 5. Make a better map. Load a selection of hurricanes with 
#     low pressure, another selection with higher pressure,
#     and another with the highest pressure. Plot each group
#     using different symbol sizes and colors. Low pressure
#     means the hurricane is stronger!


# How do I wrap these db connections and sql call in a function?


dbc = psycopg2.connect(database="geo826dd",  user="geo826dd", password="saS7ADap")

### NEW CALL###
Lcurs2 = dbc.cursor() # creates pressure to select below average pressure
Lcurs2.execute("SELECT * FROM cane WHERE press < 980") #("SELECT avg(press) FROM cane WHERE press <> -1") works in psql doesn't work through psycopg2 
Lresult = Lcurs2.fetchall() #dump query into variable
Lhcanes = geometrywk7.MultiPoint(Lresult) #This may be unnecessary
Lcanes = converter(Lhcanes) #converts tuples to lists and converters lat/lon to x/y and x/y to discrete point
mlcanes = geometry.MultiPoint(Lcanes) #multipoint class to be drawn



### NEW CALL##
Hcurs2 = dbc.cursor()#creates cursor to select above average values
Hcurs2.execute("SELECT * FROM cane WHERE press > 980")
Hresult = Hcurs2.fetchall()
Hhcanes = geometrywk7.MultiPoint(Hresult)
Hcanes= converter(Hhcanes)
mHcanes = geometry.MultiPoint(Hcanes)



### NEW CALL##
lowcurs2=dbc.cursor() # creates cursor to select the lowest pressure
lowcurs2.execute("SELECT * FROM cane WHERE press = 888")# I tried to do this but it wouldn't let me. If I ran it in psql it worked so that's where 888 came from("SELECT * FROM cane WHERE press = (SELECT min(press) FROM cane WHERE press > 0")
lowresult = lowcurs2.fetchall()
lowcane = geometrywk7.MultiPoint(lowresult)
lowestcane = converter(lowcane)
mlowcane = geometry.MultiPoint(lowestcane)


coasts.draw(mapwin2, 'white', 1) #draws coast
All.draw(mapwin2,'blue',2) #draws all hurricanes
mlcanes.draw(mapwin2,'green',2) # draws below average pressure hurricanes
mHcanes.draw(mapwin2,'yellow',2) # draws above average pressure hurricanes
mlowcane.draw(mapwin2,'red',5) # draws the lowest/most powerful hurricane.


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

