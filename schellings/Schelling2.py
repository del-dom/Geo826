#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      delpo_000
#
# Created:     12/11/2014
# Copyright:   (c) delpo_000 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import matplotlib.colors as col
import itertools
import random
from random import randint
import copy
import time 
import os 
import shutil
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, mm, inch, pica
import collections
from collections import Counter

folder = 'C:\pythons_projects\schellings\output' #output location for the plots at each timeset
imageDirectory = 'C:\pythons_projects\schellings\output\images'
outputPDFName = 'C:\pythons_projects\schellings\output\pdf'
simfolder = 'C:\pythons_projects\schellings\output\Schelling_Output_Similarity'
outputname ='C:\pythons_projects\schellings\output\simcombined'

class Schelling:
    def __init__(self,  width = 50, height = 50, empty_ratio = 0.3, similarity_threshold= 0.3, n_iterations = 400, races =4, rankhomevalue = 1,  show = True, hide= True):
        self.width = width
        self.height = height
        self.winXY = (self.width,self.height)
        self.rank = rankhomevalue
        self.rawraces = races
        self.empty_ratio = empty_ratio
        self.similarity_threshold = similarity_threshold
        self.n_iterations = n_iterations
        self.empty_houses = []
        self.agentsrace = {}
        self.agentsrank = {}
        self.agents = {} 
        self.homevalue = rankhomevalue
        self.homevalues = {}
        self.neighborsdict = collections.defaultdict(list)
        self.show = show
        self.all_houses = list(itertools.product(range(self.width),range(self.height)))
        self.hide = hide

    def neighbors(self):
      	for records in self.all_houses:
      	  self.neighborsdict[records].append((records[0]+1,records[1]+1))
      	  self.neighborsdict[records].append((records[0] - 1,records[1] - 1))
      	  self.neighborsdict[records].append((records[0],records[1]-1))
      	  self.neighborsdict[records].append((records[0]+1,records[1]-1))
      	  self.neighborsdict[records].append((records[0]-1,records[1]))
      	  self.neighborsdict[records].append((records[0]+1,records[1]))
      	  self.neighborsdict[records].append((records[0]-1,records[1]+1))
      	  self.neighborsdict[records].append((records[0],records[1]+1))
      	print "Neighbors made"
    
    def houses(self):
        random.shuffle(self.all_houses) # shuffles the list of houses in place
        self.n_empty = int( self.empty_ratio * len(self.all_houses) )# creates the number of empty houses based on the ratio of empty houses * the number of houses
        self.empty_houses = self.all_houses[:self.n_empty] #populates the empty houses with randomly located homes 
        #print self.empty_houses
        self.remaining_houses = self.all_houses[self.n_empty:] 
        print "Vacancies made"
      
      
    def populate(self):    
        houses_by_rank = [self.remaining_houses[i::self.rank] for i in range(self.rank)] # assigns the houses to be a number 
        houses_by_race = [self.remaining_houses[i::self.rawraces] for i in range(self.rawraces)]
        for i in range(self.rank):#creates agents for each race where the coordinates act as the dictionary key and the value is the rank code
            self.agentsrank = dict(self.agentsrank.items() + dict(zip(houses_by_rank[i], [i+1]*len(houses_by_rank[i]))).items())
        for i in range(self.rawraces):
	           self.agentsrace = dict(self.agentsrace.items() + dict(zip(houses_by_race[i], [i+1]*len(houses_by_race[i]))).items())
        for key in self.agentsrace:
                self.agentsrace[key] *=  10
                self.agents = dict(self.agentsrace.items() + self.agentsrank.items() + [(k, self.agentsrace[k] + self.agentsrank[k]) for k in set(self.agentsrace) & set(self.agentsrank)])
        print "Homes Populated"
    
    def is_unhappy(self, x, y):
        attributes = self.agents[(x,y)]
        count_similar = 0
        count_different = 0 # these if/else statements go to each neighboring "cell" and if the attributes value is the same.
        
        for record in self.neighborsdict[(x,y)]:
	        try:
	           if self.agents[record] not in self.empty_houses:
	               if self.agents[record] == attributes:
		              count_similar += 1
	               else:
		              count_different +=1
	        except:
	            pass

        if (count_similar+count_different) == 0:
            return False
        else:
            return float(count_similar)/(count_similar+count_different) < self.similarity_threshold 
        
    def calculate_similarity(self, x,y):
      similarity = []
      attributes = self.agents[(x,y)]
      count_similar = 0
      count_different = 0
      for record in self.neighborsdict[(x,y)]:
	  try:
	    if self.agents[record] not in self.empty_houses:
	      if self.agents[record] == attributes:
		count_similar += 1
	      else:
		count_different +=1
	  except:
	    pass
          try:
               similarity.append(float(count_similar)/(count_similar+count_different))
          except:
               similarity.append(1)
      return sum(similarity)/len(similarity)
    
    def direct(self):
      try:
        os.mkdir(folder)
      except OSError:
        shutil.rmtree(folder)
        os.mkdir(folder)
      try:
        os.mkdir(simfolder)
      except OSError:
        shutil.rmtree(simfolder)
        os.mkdir(simfolder)
      print "Directories made"

	
            
    def update(self):
    	similarity = []
    	plt.show()
    	fig, ax = plt.subplots()
    	self.plot('Schelling Model Initial Conditions', str(0))
        for i in range(self.n_iterations): # runs the update as a single batch based on the iterations specified	    
            self.old_agents = copy.deepcopy(self.agents) #creates a new object as an identical copy of the agents
            n_changes = 0 #counter to track the amount of change in the iteration
            similarity = []
            for agent in self.old_agents: #starts looping through the past distribution
                if self.is_unhappy(agent[0], agent[1]): # passing X,Y's to be checked in the above function
                    agent_attributes = self.agents[agent] # calls the attributes value of the agent                    
                    placeholder = randint(0, len(self.empty_houses)-1)
                    empty_house = self.empty_houses[placeholder]
                    self.agents[empty_house] = agent_attributes #moves the the household by assigning neighboring empty home to be same attributes
                    del self.agents[agent] # deletes the X,Y for the attributes
                    self.empty_houses.remove(empty_house) # Removes the now occupied house from the list of potential homes
                    self.empty_houses.append(agent) # adds the now vacant home to the list of empty homes
                    n_changes += 1
            for agent in self.agents:
                similarity.append(self.calculate_similarity(agent[0], agent[1]))
            print 'The mean similarity to neighbors is: ' + str(round(sum(similarity)/len(similarity),3))
            print 'This is iteration:' + str(i+1)
            print "Number of changes made: ", n_changes #prints the number of changes made
            if self.hide == True:
                if (i+1) % 25 == 0 or i+1 == self.n_iterations or n_changes == 0: 
                    self.plot('Schelling Model at timestep:' + str(i+1), i+1)
    		if self.show == True:
    		  plt.draw()	
    	    else:
    	      self.plot('Schelling Model at timestep:' + str(i+1), str(i+1) )
            if self.show == True:
                plt.draw()
    	    if n_changes == 0: # loop break if stability reached
              break



    def plot(self, title, filename):
        #plt.ion()
        fig, ax = plt.subplots()
        #If you want to run the simulation with more than 7 colors, you should set agent_colors accordingly
        agent_colors = {11:'#00ff00', 12:'#00b200', 13:'#007f00', 14:'#004c00', 15:'#001900', 
			21:'#ff0000', 22:'#cc0000', 23:'#990000', 24:'#660000', 25:'#330000',
			31:'#0000ff', 32:'#0000cc', 33:'#000099', 34:'#000066', 35:'#000033',
			41:'#e5e500', 42:'#b2b200', 43:'#7f7f00', 44:'#4c4c00', 45:'#191900',
			51:'#d3d3d3', 52:'#939393', 53:'#696969', 54:'#3f3f3f', 55:'#151515'}
        for agent in self.agents:
	  ax.scatter(agent[0], agent[1], s=self.width/(self.height/10), color=agent_colors[self.agents[agent]])
        ax.set_title(title, fontsize=10, fontweight='bold')
        ax.set_xbound([0, self.width])
        ax.set_ybound([0, self.height])
        ax.set_xticks([])
        ax.set_yticks([])
        plt.savefig(folder + str(filename) + '.jpg')
        print "Distribution saved"
        #plt.show()
        #plt.plot()
        #plt.draw()
    
    def simplot(self,title,filename,similarity):
      plt.ion()
      fig, ax = plot()
      plt.plot(similarity_threshold_ratio.keys(), similarity_threshold_ratio.values(), 'ro')
      ax.set_title('Similarity Threshold vs. Mean Similarity Ratio', fontsize=15, fontweight='bold')
      ax.set_xlim([0, 1])
      ax.set_ylim([0, 1.1])
      ax.set_xlabel("Similarity Threshold")
      ax.set_ylabel("Mean Similarity Ratio")
      plt.savefig(simfolder + str(filename) + '.jpg')
      plt.draw()
    
        
    def makepdf(self, imageDirectory, outputPDFName):
      dirim = str(imageDirectory)
      output = str(outputPDFName)
      width, height = (900,900)
      height, width = (900,900)
      c = canvas.Canvas(output, pagesize=(900,900))
      try:
	for root, dirs, files in os.walk(dirim):
	    for name in sorted(files):
		lname = name.lower()
		if lname.endswith(".jpg") or lname.endswith(".gif") or lname.endswith(".png"):
		    filepath = os.path.join(root, name)
		    c.drawImage(filepath, inch, inch * 1)
		    c.showPage()
		    c.save()
	print "PDF Created"
      except:
	print "Failed creating PDF" 
	
    def makepdf2(self,simfolder,outputname):
      dirim = str(simfolder)
      output = str(outputname)
      width, height = (900,900)
      height, width = (900,900)
      c = canvas.Canvas(output, pagesize=(900,900))
      try:
	for root, dirs, files in os.walk(dirim):
	    for name in sorted(files):
		lname = name.lower()
		if lname.endswith(".jpg") or lname.endswith(".gif") or lname.endswith(".png"):
		    filepath = os.path.join(root, name)
		    c.drawImage(filepath, inch, inch * 1)
		    c.showPage()
		    c.save()
	print "PDF Created"
      except:
	print "Failed creating PDF" 



        
'''   
    def makeworld(self):
	self.all_houses = list(itertools.product(range(self.width),range(self.height)))
        self.homevalues = self.all_houses[i::self.homevalue] for i in range(self.homevalue)]
'''




      

        
similarity_threshold_ratio = {}

schelling = Schelling(5000, 5000, 0.3, 0.3, 400000, 5, 5,  True, True)
schelling.houses()
schelling.neighbors()
schelling.populate()
schelling.direct()
schelling.update()
schelling.makepdf2(imageDirectory, outputPDFName )
#similarity_threshold_ratio = schelling.similarity()

'''
fig, ax = plt.subplots()
plt.plot(similarity_threshold_ratio.keys(), similarity_threshold_ratio.values(), 'ro')
ax.set_title('Similarity Threshold vs. Mean Similarity Ratio', fontsize=15, fontweight='bold')
ax.set_xlim([0, 1])
ax.set_ylim([0, 1.1])
ax.set_xlabel("Similarity Threshold")
ax.set_ylabel("Mean Similarity Ratio")
plt.savefig('schelling_segregation_measure.png')
plt.show()

fig, ax = plt.subplots()
plt.plot(similarity_threshold_ratio.keys(), similarity_threshold_ratio.values(), 'ro')
ax.set_title('Similarity Threshold vs. Mean Similarity Ratio', fontsize=15, fontweight='bold')
ax.set_xlim([0, 1])
ax.set_ylim([0, 1.1])
ax.set_xlabel("Similarity Threshold")
ax.set_ylabel("Mean Similarity Ratio")
plt.savefig('schelling_segregation_measure.png')
plt.show()
'''