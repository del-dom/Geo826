#!/usr/local/bin/python
#drawCoast.py
#
# A python script that draws national boundaries 
# in North America, the Caribbean, and northern 
# South America. 
#
# The data are projected in Mercator (spherical), 
# units meters, Central Meridian at 0.
#
# written by A. Shortridge, 3/2007, 3/2009, 10/2014


# More modularization! There is a folder called 
# vector in the working directory. It has Python 
# modules in it we want to use to draw stuff.
from vector import geometry
from vector import GISgraphics

def importTextMultilines(filename):
    '''Loads an ascii polyline file.
    
    First line is a header to ignore. Rest is space delimited with 
    eastings and northings. Lines with NA NA separate polylines.
    This polyline file format is used for some spatal data in R.'''
    
    plDict = {}   # an empty dictionary
    value = []    # An empty list
    linenum = 1
    f = open(filename, 'r')
    f.readline()   # Read and ignore the first line
    textline = f.readline()
    
    while textline != '':
        if textline.startswith('NA'):
            if len(value) > 1:      # No single point 'lines'!
                plDict[linenum] = value
            value = []
            linenum = linenum + 1
            textline = f.readline()
        else:
            linelist = textline.split()
            value.append((float(linelist[0]), float(linelist[1])))
            textline = f.readline()
    f.close()
    return plDict

def exportTextMultilines(inDict, filename):
    '''Writes an ascii polyline file.
    First line is a header. Rest is space delimited with eastings and 
    northings. Lines with NA NA separate polylines.
    This polyline file format is used for some spatal data in R.'''
    f = open(filename, 'w')
    f.write('"x" "y"\n')
    for line in inDict.values():
        for coord in line:
            f.write("%i %i\n" % (coord[0], coord[1]))
        f.write("NA NA\n")
    f.close()


############################
# Actual code to do things #
# starts at this point.    #

fn = 'amer_tropics.csv'
coastDict = importTextMultilines(fn)

# Get the coast/boundary dictionary into a MultiLineString format
# This should probably be integrated into the Geometry class.
lsList = []
for line in coastDict.values():
    pts = []
    for p in line:
        pts.append(geometry.Point(p[0], p[1]))
        lsList.append(geometry.LineString(pts))  # List of Points
    

coasts = geometry.MultiLineString(lsList)

# Now actually create the window and draw stuff.
mapwin = GISgraphics.MapWindow(': Central America', winXY=(400,400),\
mapSize=coasts.envelope)

coasts.draw(mapwin, 'white', 1)
a = raw_input('Hit Enter to Quit ')
