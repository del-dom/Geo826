####################
## III. Exercises ##

''' 1. Your task is to develop a module with a handful of useful functions for
working with lat/lon data. This module has already been started for you; it's
called latlontools.py.

The module should contain functions for converting degrees minutes seconds
(dms) coordinates to dd, and vice versa. You've already written code to do
these; now you simply have to write them as functions in latlontools.py. They
should take a coordinate pair as input and return a (converted) coordinate pair.

In addition, you need to write a function that takes two lat/lon (in decimal
degrees) points (e.g. EL and GR) and returns the distance in km between them.
It'd be nice to use Documentation Strings (Byte of Python chapter 7) so someone
typing  help(haversine) (or whatever you call it) gets a description of what
it does.

Here's more background on that distance function.
Suppose we want to calculate crow's flight distances between EL and each of the
other cities from the dataset used in class. Your Euclidean distance function might
be really handy... But is it ok to run it on lat/lon values? HINT: The answer is NO!

Either we project these things, or we calculate spherical distance instead. I suggest 
the latter. The Haversine formula can be employed to calculate distance on the surface
of a sphere. For most cases, this is accurate enough. This site (found via Google):
http://www.movable-type.co.uk/scripts/GIS-FAQ-5.1.html
describes an algorithm to calculate spherical distance, given two lat/lon pairs.

Test your module with the small latlontest.py program!'''
EL = ((42,44,9), (84,29,4))
Det = ((42,22,59), (83,6,8))
Kal = ((42,16,29), (85,35,18))
AA = ((42,16,31), (83,43,51))
Lan = ((42,42,33), (84,33,14))
GR = ((42,57,41), (85,39,21))
SSM = ((46,29,4), (84,21,56))

def dms2dd((a,b,c)):
	Dega = a
	Minb = b/float(60)
	Secc = c/float(3600)
	ddlat = round((Dega+Minb+Secc),5)
	return(ddlat)
	
#def dms2dd((a,b,c),(x,y,z)): #for converting the coordinate pair at the same tiem
	#Dega = a
	#Minb = b/float(60)
	#Secc = c/float(3600)
	#ddlat = round((Dega+Minb+Secc),5)	
	#Degx = x
	#Miny = y/float(60)
	#Secz = z/float(3600)
	#ddlon = round((Degx+Miny+Secz),5)
	#return(ddlat,ddlon)
	
def dd2dms(x):
	Degx = int(x) #removes integer 
	msx = abs(60 * float(x % Degx)) #pulls out the decimal while making it positive
	Minx = int(msx) #assigns decimal value to minutes
	Secx =  round(abs(60 * (msx - Minx)),0) #creates seconds while making positive and rounded to the 5th place 
	dmsx = (Degx,Minx,Secx)	
	return(dmsx)
		
	#def dd2dms(x,y):#If converting the coordinate pair at the same time
	#Degx = int(x) #removes integer 
	#msx = abs(60 * float(x % Degx)) #pulls out the decimal while making it positive
	#Minx = int(msx) #assigns decimal value to minutes
	#Secx =  round(abs(60 * (msx - Minx)),5) #creates seconds while making positive and rounded to the 5th place 
	#dmsx = (Degx,Minx,Secx)	
	#Degy = int(y)
	#msy = abs(60 * float(y % Degy))
	#Miny = int(msy)
	#Secy = round(abs(60 * float(msy - Miny)),5)
	#dmsy = (Degy,Miny,Secy)
	#return (dmsx,dmsy)
	
def haversine(p1,p2):
	import math
	earthradius = 6371.009
	rc = 0.017453293
	p1lat = math.radians(p1[0]) 
	p1lon = math.radians(p1[1])
	p2lat = math.radians(p2[0]) 
	p2lon = math.radians(p2[1]) 
	dlat = p2lat - p1lat
	dlon = p2lon - p1lon
	a = (math.sin(dlat/2)**2) + (math.cos(p1lat)) * (math.cos(p2lat)) * (math.sin(dlon/2)**2)
	c = 2 * math.asin(a**.5)
	d = earthradius * c
	return(d)
	

# 2. Write code to generate a more complex data structure using the China provinces
# data. In the code above, a list of dictionaries was constructed. Convert this to a
# dictionary of dictionaries, where the key is the name of the province. This will
# allow you to request all data about a province just by stating its name, e.g.:
chinaDict['Hubei']  # should return data for Hubei, no need to loop through all records!

import csv

inf = open('china_population.txt', 'r') 
reader = csv.reader(inf)  
for line in reader:
    print line  

inf.close()
inf = open('china_population.txt', 'r')
dreader = csv.DictReader(inf)

china = []
for line in dreader:
    china.append(line)

chinaDict = {}

#my code begins.
for i in china:
   chinaDict[i["Province"]] = {"population" : i['Population'], "percent of total in 2000": i["percent of total in 2000"], "percent of total in 2010": i["percent of total in 2010"]}



# Fill in the rest (just two lines of code are needed! Hint: see Byte of Python Ch 12

# 3. The following is a raster land cover map (1=urban, 2=agriculture, 3=water):
# 2 2 2 2 2
# 3 3 2 2 2
# 3 3 1 1 2
# 3 1 1 2 2
# 2 2 1 2 2

# Develop a data structure (hint - don't use dictionaries!) for this raster.
# Then write a function called countCells that takes two arguments: the
# raster and a land cover code. It should return the number of cells in
# the raster with that code. For example, countCells(rast, 1) should
# return 5, since there are 5 cells with the value 1.

raster = [ 2,2,2,2,2,3,3,2,2,2,3,3,1,1,2,3,1,1,2,2,2,2,1,2,2]


def countCells(x,y):
    print x.count(y)