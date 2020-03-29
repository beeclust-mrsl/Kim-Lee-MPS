import numpy as np
import math


class kimLee():

	def __init__(self, bots, lines, botpos ,pop):
	

		#5 lines represented by their start pose and end pose
		self.lines = lines
		self.numLines = np.shape(self.lines)[0]

		#we have only 3 bots
		self.bots = bots

		#making population and selecting best population using genetic algorithm
		#now cost of these lines will act as weights so we will arrange these weights(costs) in group of three lines for 
		#let initial pop has three chromosomes as array of three cost in pattern (1,2,3)  (2,3,4)   (3,4,5) according to 3 bots 
		self.botspos=np.empty((0, 1, 2), float)
		#Assign values of botpos:


		self.group = np.empty((0, 2, 2), float)
		self.group = [self.group for i in range(self.bots)]

		for index, val in enumerate(self.lines):
			self.group[index % self.bots] = np.append(self.group[index % self.bots], np.array([val]), axis = 0)

		print(self.group)

	    self.pop = np.empty([1,numpop],dtype =float)

	    self.pop[0] = self.group  #first pop is initial set of group



 	def cal_cost(group,groupnum):

 		oldend = botpos[groupnum]
		totaldist=0
		dist=0
		startpose = [0,0]
		endpose = [0,0]
		dtemp = #some big val 

	#right now its 3 seperate lines ,will change it for connected lines 
		for i in range(0,self.bots):
			for j in range(0,sel.bots):
				startpose = group[j][0]
				endpose = group[j][1]
				dist = math.sqrt( (endpose[0]-oldend[0])**2 + (endpose[1]-oldend[1])**2 )
				
				if (dist<dtemp ):
					dtemp=dist
					nearend = endpose
	
			
			totaldist = totaldist+dtemp
			oldend = nearend

		return totaldist

# #initial pop will be like pop=[cost1,cost2,cost3]


#Evaluation (can find the pop with bestcost and hence bestpop....Fitness check)
	def Eval(pop):
		for j in pop
			group=pop[j]
			for i in range(0,3):           
				cost[i] = cal_cost(group[0])	
			mcost = max(cost)
			bestcost = mcost
			for k in range(0,3):
				if (cost[k]<bestcost):
					bestcost=cost[k]
					idx=k
					bestpop=j+1
			bestparents = np.append(bestparents,group[idx]) 		

		return bestparents


	def crossover(parents,offspring_size):
 		offspring=np.empty(offspring_size)	#initialise 
 		crossover_pt=numpy.uint8(offspring_size[1]/2)

 		for k in range(offspring_size[0]):
 			parent1_id = k%parents.shape[0]
 			parent2_id = (k+1)%parents.shape[0]
 			offspring[k,0:crossover_pt]=parents[parent1_id,0:crossover_pt]
 			offspring[k,crossover_pt]=parents[parent2_id,crossover_pt:]

 		return offspring

#adding variations to offspring using mutation

	def mutation(offspring):
		for idx in range(offspring.shape[0]):
			random_value = np.random.uniform(-1.0,1.0,1)
			offspring[idx,4] = offspring[idx,4] + random_value
		return offspring


if __name__ == '__main__':
	lineSet = np.array([
				[(1,11), (11,1)],
				[(2,22), (22,2)],		
				[(3,33), (33,3)],
				[(4,44), (44,4)],
				[(5,55), (55,5)]
				])

	test = kimLee(bots = 3, lines = lineSet)

	
 	
 	#defining the pop for first gen
 	grp = test.self.group

 	

 	
 		

	 		



	
	 




