'''
sleepsick.py

Implements significant elements of a complex spatial agent based model for Sleeping Sickness.
Roughly based on a published model by G. Muller et al. (2004) An agent-based model of sleeping 
sickness: simulation trials of a forest focus in southern Cameroon. Comptus Rendus Biologies 327: 1-11.

This code develops a set of classes for implementing a sleeping sickness
model with three classes: humans, pigs, and flies. It also introduces a 
variable landscape: Town and Forest, with different parameters for 
each agent.

A. Shortridge, 4/2009, 11/2014
'''

# Some global parameters
FLY_INFECT_RATE = 0.6
HUMAN_INFECT_RATE = 0.6
PIG_INFECT_RATE = 0.6

class World():
    '''A class for the world space of the sleeping sickness model.
    By default, the world is young and has three environments, 
    village(0),forest (1),plantation(2).'''
    def __init__(self, age=0, environments=[0,1,-1], numPeople=20, numPigs=50, numFlies=100):#----MODIFIED----
        self.age=age
        self.environments = environments
        # The following lines set up groups of people, pigs, and flies,
        # with hopefully reasonable parameter values
        self.village = Flock([Human(0,0,[(50,50),(60,40),(80,20)]) for p in range(numPeople)]) #(self, age, environment, moveProbList, infected)#----MODIFIED----
        self.herd = Flock([Pig(0,1,[(40,60),(70,30),(50,50)]) for p in range(numPigs)])#----MODIFIED----
        self.swarm = Flock([Fly(0,1,[(60,40),(75,25),(50,50)]) for f in range(numFlies)])#----MODIFIED----
        for n in range(5):
            self.swarm.flock[n].infected = True  # Infect 5 flies.
        self.statistics = [self.calcStats()]
    
    def critterNeighbors(self, flock):
        '''For each individual in flock, calculate the critters in its environment.
        Store them in a neighbors list.'''
        self.population = []
        index = 0
        for critter in flock.flock:
            critter.neighbors = []
            for p in self.village.flock:
                if p.location == critter.location:
                    critter.neighbors.append(p)
            for p in self.herd.flock:
                if p.location == critter.location:
                    critter.neighbors.append(p)
            for f in self.swarm.flock:
                if f.location == critter.location:
                    critter.neighbors.append(f)
            
    def __str__(self):
        about = 'Day ' + str(self.age) + '\n' + str(self.village) + '\n' + str(self.herd) + '\n' + str(self.swarm)
        return about
    
    def calcStats(self):
        '''Keep track of population and infected individual totals.'''
        totalHumans = len(self.village)
        infectedHumans = self.village.totalInfected()
        totalPigs = len(self.herd)
        infectedPigs = self.herd.totalInfected()
        totalFlies = len(self.swarm)
        infectedFlies = self.swarm.totalInfected()
        return {'totalHumans' : totalHumans, 'infectedHumans' : infectedHumans,
                'totalPigs' : totalPigs, 'infectedPigs' : infectedPigs,
                'totalFlies' : totalFlies, 'infectedFlies' : infectedFlies}
    
    def getStats(self):
        '''Return a string with the statistics.'''
        statString = 'Day\tPpl\t(ill)\tPigs\t(ill)\tFlies\t(ill)\n'
        d = 0
        for day in self.statistics:
            statString += str(d)+'\t'+str(day['totalHumans'])+'\t' + str(day['infectedHumans'])+'\t' + str(day['totalPigs'])+'\t' + str(day['infectedPigs'])+'\t' + str(day['totalFlies'])+'\t' + str(day['infectedFlies'])+'\n'
            d += 1
        return statString
    
    def advance(self):
        '''Advance the simulation one step in time.'''
        self.critterNeighbors(self.swarm) # calculate neighbors for each fly
        self.swarm.advance()
        self.village.advance()
        self.herd.advance()
        self.age += 1
        print self
        self.statistics.append(self.calcStats())

class Critter():
    '''A Class for things that move around.'''
    def __init__(self, age, environment, moveProbList, infected=False, infect_age=0):
        self.age = age
        self.location = environment
        self.infected = infected
        self.moveProbList = moveProbList
        self.infect_age = infect_age
    
    def __str__(self):
        about = 'age: ' + str(self.age) + '; infected: ' + str(self.infected) + '; environment: ' + str(self.location)
        return about
     
    def move(self):
        '''Change location of the critter. Environment argument is not used here.'''
        from random import randint
        probs = self.moveProbList[self.location]
        if randint(0,100) > (probs[0]):  # it changes environment. #----MODIFIED----
	  if self.location == 2:#----MODIFIED----
	    self.location = 0#----MODIFIED----
	  if self.location==1:#----MODIFIED----
	    self.location = 0#----MODIFIED----
	  if self.location ==0:#----MODIFIED----
	    self.location = randint(1,2)#----MODIFIED----


class Human(Critter):
    '''A Class for people.'''
    def __init__(self, age, environment, moveProbList, infected=False, infect_age=0):#----MODIFIED----
        Critter.__init__(self, age, environment, moveProbList, infected, infect_age) # first init ''critter
        
    def infect_age(self):
      if self.infected == True:
	self.infect_age = self.infect_age+1

class Pig(Critter):
    '''A Class for pigs.'''
    def __init__(self, age, environment, moveProbList, infected=False):
        Critter.__init__(self, age, environment, moveProbList, infected) # first init critter

class Fly(Critter):
    '''A Class for tsetse flies.'''
    def __init__(self, age, environment, moveProbList, infected=False):
        Critter.__init__(self, age, environment, moveProbList, infected) # first init critter
    
    def targetCritter(self, world):
        '''Identify a target for biting. This requires some knowledge of the 
        environment.'''
        
    def move(self):
        '''Overrides Critter.move. This moves but also feeds the individuals.
        I don't really like combining these things - sloppy coding design.'''
        from random import randint
        
        # Target and Bite!
        # First create a list of valid targets in the same location as the fly.
        targets = [n for n in self.neighbors if not isinstance(n, Fly)]
        if len(targets) > 0:  # if there are targets to bite
            victim = randint(0,len(targets)-1)
            self.bite(targets[victim])
        # Now move the individuals
        probs = self.moveProbList[self.location]
        if randint(0,100) > (probs[0]):  # it changes environment.
	  if self.location == 2:
	    self.location = 0
	  if self.location==1:
	    self.location = 0
	  if self.location ==0:
	    self.location = randint(1,2) 
	      
        
    
    
    def bite(self, critter):
        '''Flies bite other critters. They can get infected that way, 
        and infect others with their bite.'''
        from random import randint
        import copy
        if critter.infected:
	  if self.age <= 4: #-----MODIFIED----
            if randint(0,100) < (FLY_INFECT_RATE * 100):
                self.infected = True
          else:
	    if randint(0,100) < ((FLY_INFECT_RATE * 1.5) * 100):
                self.infected = True
        if self.infected:
            if isinstance(critter, Human):
	      if self.infect_age < 90: #----MODIFIED----
                infectionRate = (HUMAN_INFECT_RATE * .5)
	      else:
		infectionRate = HUMAN_INFECT_RATE
	    
            elif isinstance(critter, Pig):
                infectionRate = PIG_INFECT_RATE
            print 'infected fly about to bite!'
            if randint(0,100) < (infectionRate * 100):
                critter.infected = True


    

class Flock:
    '''A group of critters of the same type. Useful for 
    working with large numbers of things.'''
    
    def __init__(self, critterList):
        self.flock = critterList
        if isinstance(critterList[0], Human):
            self.species = 'human'
        elif isinstance(critterList[0], Pig):
            self.species = 'pig'
        elif isinstance(critterList[0], Fly):
            self.species = 'fly'
    
    def __len__(self):
        '''This overrides the len operator to work on this class.'''
        return len(self.flock)
    
    def totalInfected(self):
        '''count the total number of infected critters in the flock.'''
        total = 0
        for c in self.flock:
            if c.infected:
                total = total + 1
        return total
    
    def totalLocation(self):
        '''count the total number of critters in each environment type.'''
        total = [0,0,0]
        for c in self.flock:
            total[c.location] +=1
        return total
    
    def __str__(self):
        about = str(len(self)) + ' critters of type ' + self.species + '. ' + str(self.totalInfected()) + ' are infected. ' + str(self.totalLocation()[1]) + ' are in the forest.' + str(self.totalLocation()[2])  + ' are at the plantation'
        return about
    
    def advance(self):
        '''Go forward in time with the flock. Move and age the individuals.'''
        for i in self.flock:
            i.age += 1
            i.move()

    
    

