# class4_homework.py
# Feel free to work with other students in the class on these. Just be 
# sure you indicate that you got help on them, and who helped you!
# written by A. Shortridge

# 1. WRITE CODE THAT WILL GRAPHICALLY DISPLAY THE LENGTH IN KM FOR A DEGREE OF 
# LONGITUDE AT THE FOLLOWING LATITUDES: 0, 10, 20, 30, 40, 50, 60, 70, 80


#I almost certainly made this more difficult than it needed to be.

import math
import pylab   
import csv
import pylab
import pl 


lat = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90] 

def datlat(r, axisShift = False):
   
    er = 6371.009 # Earth's radius
    lataltered = [] #empty list for earths radius
    opp = [] # empty list for km from equator
    y = [] #empty list for latitude
    for i in r: #interates through input
	s1 = er * (math.cos(math.radians(i))) #calculates the cosine. Degrees converted to radians 1st
	lataltered.append(s1) #appends lataltered with xcoord values
	y.append(i)
	#y.append(math.radians(i)) #If you want Y axis to be in radians 
    for z in r: # Used a modified haversine in order to find the distance traveled along a longitudinal line not just the flat plane distance.
	p1lat = 0 #held as a constant to measure from
	p1lon = 1 # this value shouldn't really matter as long as both LON values are the same.
	p2lat = math.radians(z) 
	p2lon = 1
	dlat = p2lat - p1lat
	dlon = p2lon - p1lon
	a = (math.sin(dlat/2)**2) + (math.cos(p1lat)) * (math.cos(p2lat)) * (math.sin(dlon/2)**2)
	c = 2 * math.asin(a**.5)
	d = er * c
	opp.append(d)

    pylab.plot(lataltered, y, 'ro')
    pylab.plot(lataltered, y, label = "Earths Radius")
    pylab.bar(opp,y) # left as empty bars so that the rest of the graph is visible
    pylab.plot(opp,y, label = "Km from equator") #label = adds object for legend to reference
    pylab.xlabel("Distance in Km") 
    pylab.ylabel("Degrees Latitude")
    pylab.legend(loc = 'upper center') # loc = '' tells the legend where to go
    pylab.title("Earth's radius Vs Km from equator")
    if axisShift: #sizes viewing window
        pylab.axis([min(x)-1,max(x)+1,  min(y)-1, max(y)+1])
    
    pylab.show() #shows plot
	
	
	
	
    



# 3. THE PL MODULE LETS YOU DRAW POINTS AND LINES, BUT NOT AT THE SAME TIME.
# WRITE A NEW FUNCTION THAT WILL DRAW POINTS AND LINE ON A SINGLE MAP.


coordlist = ([1,2,3,4],[1,2,3,4]) # test list

def pointsandlines(coordlist): #function takes a single list arguement
    for line in coordlist: #begins loop through line 
        x = [] #empty list for x coordinates
        y = [] # empty list for Y coordinates
        for segment in line: # loops through the segments of the line
            if type(segment) == list: # if a line segment equals a list type begin the next loop
                for i in segment: # for object in list segment
                    x.append(i[0]) #append the 0th to x 
                    y.append(i[1]) # append 1st to y
            else: # if segment is not a list
                x.append(segment) #append entire segment to list
                y.append(segment) # append entire segment to list
            pylab.plot(x, y, 'rx') # plot red X's at the coordinate points in the x and y lists
            pylab.plot(x, y) # plot a line that connects the coordinates in the x an y lists
    pylab.show()

# 4. Choose ONE of the following problems to solve. If you want of course, 
# you can do both!
# B. READ "USA_MERC.CSV" IN. STORE IT AS A MULTILINES FEATURE SO
# THAT PL CAN PLOT IT AS LINES! CREATE A MAP OF THESE LINES.

#I sunk another few hours into this question and couldn't find a better solution.
#I'm not understanding how to create a new list mid-for loop so as to isolate the
#coordinate pair series that are separated by the 'NA''s
# If I could do that I would assume I would simple make a list of those lists 
#and then run it through pl.plotLines
#I left the str and float in the 3rd loop as the they must do something cause it doesn't work with it


records = []
records2 = []
with open('/home/geo826dd/week_4/usa_merc.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
	records.append(row)
	
for i in records:
    if i[0] != 'NA': # this doesn't actually parse out all 'NA''s
	records2.append(i)
	
for i in records2:
    if i[0] == str():
	float(i)
	


pl.plotLine(records2)
#will plot as a single line. 
	
	





