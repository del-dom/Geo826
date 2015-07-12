# class5_homework.py
# Feel free to work with other students in the class on these.
# Just be clear about who you got help from!. 

# 1. Write a function to find intersection points between two lineFeatures.
# Things to think about:
#     Read carefully about what I am calling a lineFeature (in intersection.py)
#     There could be more than one intersection. Return all of them.
#     There could be no intersections. Then return an empty list
#     Don't rewrite the segment intersection function! Call it inside your function.
#     Polylines are just sets of line segments. This is the key.

# My polyline intersection function is just 13 lines long (8 not counting the docstrings). 
# So this is actually a fairly small piece of code. I will assess your code's ability to
# find the intersections of the polylines called L5 and L6 in the intersection.py code.
pt1 = (1,1)
pt5 = (2,2)
pt6 = (2,3)
pt7 = (4,6)
pt8 = (6,3)
pt9 = (3,1)
pt10 = (1,4)
pt11 = (3,6)
pt12 = (4,3)
pt13 = (7,4)

l1 = [[pt1, pt5]]
l2 = [[pt7, pt8]]
l3 = [[pt1,pt2]]
l4 = [[pt3,pt4]]
l5 = [[pt1, pt5, pt6, pt7, pt8, pt9]] #l5 = [[(1,1),(2,2),(2,3),(4,6),(6,3),(3,1)]]
l6 = [[pt10, pt11, pt12, pt13]] #l6 = [[(1,4),(3,6),(4,3),(7,4)]]



def lSegInt(s1, s2, t1, t2):
    '''Function to check the intersection of two line segments. Returns 
    None if no intersection, or a coordinate indicating the intersection.
    
    An implementation from the NCGIA core curriculum. s1 and s2 are points 
    (e.g.: 2-item tuples) marking the beginning and end of segment s. t1 
    and t2 are points marking the beginning and end of segment t. Each point 
    has an x and y coordinate: (1, 3). 
    Variables are named following linear formula: y = a + bx.'''
    if s1[0] != s2[0]:                # if s is not vertical
        b1 = (s2[1] - s1[1]) / float(s2[0] - s1[0])
        if t1[0] != t2[0]:             # if t is not vertical
            b2 = (t2[1] - t1[1]) / float(t2[0] - t1[0])
            a1 = s1[1] - (b1 * s1[0])
            a2 = t1[1] - (b2 * t1[0])
            if b1 == b2:                # if lines are parallel (slopes match)
                return(None)
            xi = -(a1-a2)/float(b1-b2)  # solve for intersection point
            yi = a1 + (b1 * xi)
        else:
            xi = t1[0]
            a1 = s1[1] - (b1 * s1[0])
            yi = a1 + (b1 * xi)
    else:
        xi = s1[0]
        if t1[0] != t2[0]:            # if t is not vertical
            b2 = (t2[1] - t1[1]) / float(t2[0] - t1[0])
            a2 = t1[1] - (b2 * t1[0])
            yi = a2 + (b2 * xi)
        else:
            return(None)
    # Here is the actual intersection test!
    if (s1[0]-xi)*(xi-s2[0]) >= 0 and \
    (s1[1]-yi)*(yi-s2[1]) >= 0 and \
    (t1[0]-xi)*(xi-t2[0]) >= 0 and \
    (t1[1]-yi)*(yi-t2[1]) >= 0:
        return((float(xi), float(yi)))  # Return the intersection point.
    else:
        return(None)   

        
''' this function unpacks the multilinestring into line coordinate pairs.
This is needed so that the coordinate pairs can be passed through lSegInt'''
def split(a): #takes input
    lines = [] # empty list
    for i in range(len(a[0]) - 1): # loops through all but the last record of a 
	line = [] # empty list
	for j in (i,i+1): # j ish the oth object and i+1 is the 1st objecct thus creating a coordinate pair 
	    line.append(a[0][j]) #creates a 0112233445 sequence to the records in a
	lines.append(line)
    return lines
	    
    
sl5 = split(l5)
sl6 = split(l6) 

def intcheck(a,b):
    x = 0
    fresults = [] # empty list to append to
    for i in a: # begins the loop of sl5.The J for loop is completed before returning to this level
	for j in b: #loops can be freely nested within other loops. loop through sl6
	    z = lSegInt(i[0],i[1],j[0],j[1]) # assigning to a variable so that a check can be run
	    if z != None:
		fresults.append(z)
    while x < len(fresults):
	x += 1
    print "These lines intersect at",x,"locations.","These locations are",fresults

	
  
# 2. Load in the Hangzhou streets(hangzhou_lines.shp) shapefile. Plot it! Then figure
# out how to count the number of line intersections in it. How many are there? 


import osgeo.ogr

shpf = osgeo.ogr.Open("/home/geo826dd/week_5/hangzhou_lines.shp")

lyr = shpf.GetLayer(0)
line = lyr.GetNextFeature()
line_geom = line.GetGeometryRef()
def getLineSegmentsFromGeometry(geom):
    segList = []
    if geom.GetPointCount() > 0:
        segCoords = []
        for i in range(geom.GetPointCount()):
            segCoords.append(geom.GetPoint_2D(i))
        segList.append(segCoords)
    for i in range(geom.GetGeometryCount()):
        subGeom = geom.GetGeometryRef(i)
        segList.extend(getLineSegmentsFromGeometry(subGeom))
    return segList
    
def readShape(fn):
    import osgeo.ogr
    shpf = osgeo.ogr.Open(fn)
    lyr = shpf.GetLayer(0)
    segList = []  # This will be filled with coordinates
    for i in range(lyr.GetFeatureCount()):
        feature = lyr.GetFeature(i)
        geomObj = feature.GetGeometryRef()
        segList.append(getLineSegmentsFromGeometry(geomObj))
    return(segList)
    
ha_zh = readShape("/home/geo826dd/week_5/hangzhou_lines.shp")


flattened = []
for sublist in ha_zh:
    for val in sublist:
        flattened.append(val)

def intcheck2(a,b):
    import pylab
    import pls
    fresults = [] # empty list to append to
    for i in a: # begins the loop of sl5.The J for loop is completed before returning to this level
	for j in b: #loops can be freely nested within other loops. loop through sl6
	    for i1,i2 in zip(i[:-1],i[1:]):
		for j1,j2 in zip(j[:-1],j[1:]):
		    z = lSegInt(i1,i2,j1,j2) # assigning to a variable so that a check can be run
		    if z != None:
			fresults.append(z)
    x = len(fresults)
    pls.pointsandlines(fresults,a)
    print fresults, "These lines intersect at", x ,"locations.","These locations are above"

intcheck2(flattened,flattened)    






