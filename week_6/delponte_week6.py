# class6_homework.py
# Feel free to work with other students in the class on these.
# Just be clear about who you got help from!. 

# 1. Write a function to calculate the total length of an arc in our network 
#   data structure. That includes all the segments making up the arc!

def distance((x, y), (a, b)): #called in both lenarcnodes and lenarc.
  import math
  c = math.sqrt((x-a)**2 + (y-b)**2)
  return c
  
def lenarcnodes(data, StartNode, EndNode): #data, where you are and where you want to go. This defines an arc/line.
    import pylab
    Start = data['nodes'][StartNode]['lLst'] #finds one end of the arc
    End = data['nodes'][EndNode]['lLst'] #finds the other end
    cline = [] # the lines that the start and end node have in common
    thearc = [] # the point keys of the line in common
    cpair = [] # the points of the line in common
    length = [] # the lengths of each segment of the poly line
    x = []
    y = []
    for line in Start: #loops start
	if line in Start and  line in End: #searches for common elements in start and end
	    if line not in cline: #if the line is not already in cline
		cline.append(line) #append it
	#print cline
	if cline == []:
	    print "No line in common"
	for arc in cline: #loops through the lines in common
	    thearc.append(data['arcs'][arc]['pLst']) # a list of point keys
	    #print thearc
	    for vertices in thearc: #the exact x,y point keys are isolated
		#print vertices
		for points in vertices: # the actualy x,y tuples are looped through
		    #print points
		    if data['pts'][points] not in cpair: #if the tuple isn't in cpair append it. This is important so as to avoid duplicates. Duplicates are bad because it's a line, it shouldn't have duplicate points.
			cpair.append(data['pts'][points])
    for tup1,tup2 in zip(cpair[:-1],cpair[1:]):
	#print tup1
	#print tup2
	length.append(distance((tup1),(tup2)))
    for plot in cpair:
	x.append(plot[0])
	y.append(plot[1])
    #print x
    #print y
    if x != []:
	pylab.plot(x,y, 'ro')
	pylab.plot(x,y)
	pylab.show()
    return sum(length)
''' the above code has issues if there are multiple lines going to the same node from a single start node. The primary issue is that it returns the sum of the lengths of all arcs not individually.
This could be solved by appending the length list to a sum of length list that would be a list of lists after every loop. This isn't needed inorder to solve this particular question so I didn't fix it to do so.'''
lenarcnodes(testNet,'n1','n4')

''' built the above then I thought about question two and realized the formatting above was going to make it more difficult so I trimmed it to this'''

def lenarc(data, l): 
    #import pylab
    line = data['arcs'][l]['pLst'] 
    #print line
    cpair = [] 
    length = [] 
    #x = []
    #y = []
    for arc in line:
	#print arc
	if data['pts'][arc] not in cpair:
	    cpair.append(data['pts'][arc])
    for tup1,tup2 in zip(cpair[:-1],cpair[1:]):
	length.append(distance((tup1),(tup2)))
	#print length
    #for plot in cpair:
	#x.append(plot[0])
	#y.append(plot[1])
    #pylab.plot(x,y, 'ro')
    #pylab.plot(x,y)
    #pylab.show()	    
    return sum(length)

    
lenarc(testNet,'l6')

# 2. Write a function to store arc length in the network structure for all arcs
#    in a structure. Use function #1 to do the hard work.

def moredata(data2, dictionary):
    arc = data2[dictionary]
    for lines in arc:
	#print lines
	data2[dictionary][lines]['cost'] = (lenarc(data2,lines))
    return data2[dictionary]
    
    
moredata(testNet,'arcs')



# 3. Implement Dijkstra's shortest path algorithm on your enhanced structure!
#    the function should take the network of course, along with a start and end node,
#    and calculate the shortest route between these nodes. It should return a network 
#    data structure with the arcs along this route!

def findNbrNodes(nw, node):
    '''Find all nodes "neighboring' node, meaning that they share a common arc.
    Returns a list of dicts with keys equal to the node, and value equal to the distance.'''
    neighboringline = nw['nodes'][node]['lLst']
    Ldict = {}
    m=node
    costs =[]
    for position in range(len(neighboringline)):
	nodes = nw['arcs'][neighboringline[position]]['nLst']
	#print nw['arcs'][neighboringline[thing]]['cost']
	#print nodes
	for z in nodes:
	    if z != node:
		Ldict[m] = {z:z, 'Cost':nw['arcs'][neighboringline[position]]['cost']}
		costs.append(Ldict)
		Ldict={}  
    costs.sort(key=lambda e: e['n4']['Cost'], reverse=False) #sorts list
    return costs
    
findNbrNodes(testNet, 'n4')

def Dijkstra(nw, startNode, endNode, verbose=False):
    '''Traverses network nw, starting at startNode, until all possible nodes have been
    visited or until endNode is reached. Returns the list of nodes along the shortest path.'''
   
    visited = []  # This is a list of visited nodes. Right now it is empty!
    canVisit = [] # This is a list of nodes we can visit. Empty too!
    finished = False
   
    # Add a dict to the list for startNode. THIS IS MY ROUTE DATA STRUCTURE!
    canVisit.append({'node' : startNode, 'dist' : 0, 'route' : [startNode]})
   
    ct = []
    while len(canVisit) > 0:
	canVisit.sort(key=lambda e: e[startnode]['Cost'], reverse=False) #i'm not sure how to sort repetitively
        # Sort canVisit by distance
        currentlyAt = canVisit.pop(0)
        # pop the first record!
        # put that record in visited
        visited.appened(currentlyAt)
        if currentlyAt == endnode:
	    break #I don't know what to do here
       
        # if currentlyAt is endNode, we've found it!
       
        # Get the new nodes
       
       
        # Add the distance to get to currentlyAt to each distance in newNodes.
       
       
        # Add the route of currentlyAt to each record in newNodes
       
       
        # Check for duplicates in visited. Replace records in visited if the
        # new route is shorter. If it's not a duplicate, add it to canVisit.
       
        # to make this easier, a second list with just the node values in visited
        visitNodes = [rec['node'] for rec in visited]
        for n1 in newNodes:
       


# 4. Write a function to graphically display two networks at the same time. This is so
#    you can display a network with a shortest path route superimposed over the top.
#
# 5. Load the Hangzhou streets(hangzhou_lines.shp) shapefile. Plot it! Then convert it to
#    a network and calculate the shortest path from one node in the city to another. Turn
#    in a graphic showing your route. 


			
