import pylab
def plotLines(linelist, axisShift = False):
    '''Uses matplotlib to plot a list of polylines. If axisShift=True, shifts 
    the plot region out a bit so that all points are inside the region.
    Works on pseudo WKT line representations, in which a polyline is a list of
    lists of line segment coordinates.'''
    import pylab
    xran = []
    yran = []
    for line in linelist:
        x1 = []
        y1 = []
        if len(line) > 1:  # if this is a list of tuples
            for i in line:
                x1.append(i[0])
                y1.append(i[1])
        else: # assume it contains a list of tuples as the 0th element
            for i in line[0]:
                x1.append(i[0])
                y1.append(i[1])
        xran.extend([max(x1), min(x1)])
        yran.extend([max(y1), min(y1)])
        pylab.plot(x1, y1)
    
    if axisShift is True:
        pylab.axis([min(x1ran)-1,max(x1ran)+1,  min(y1ran)-1, max(y1ran)+1])
        

def plotPts(coordlist, axisShift = False):
    '''Uses matplotlib to plot a list of x,y coordinates.
    If axisShift=True, shifts the plot region out a bit so 
    that all points are inside the region.'''
    
    x = []
    y = []
    for i in coordlist:
        x.append(i[0])
        y.append(i[1])
    pylab.plot(x, y, 'ro')
    if axisShift:
        pylab.axis([min(x)-1,max(x)+1,  min(y)-1, max(y)+1])
 
    
def pointsandlines(points,lines):
    plotPts(points)
    plotLines(lines)
    pylab.show()

    