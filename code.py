import numpy as np
import math


class kimLee():

	def __init__(self, bots, lines):
	

		#5 lines represented by their start pose and end pose
		self.lines = lines
		self.numLines = np.shape(self.lines)[0]

		#we have only 3 bots
		self.bots = bots

		#making population and selecting best population using genetic algorithm
		#now cost of these lines will act as weights so we will arrange these weights(costs) in group of three lines for 
		#let initial pop has three chromosomes as array of three cost in pattern (1,2,3)  (2,3,4)   (3,4,5) according to 3 bots 
		
		self.group = np.empty((0, 2, 2), float)
		self.group = [self.group for i in range(self.bots)]

		for index, val in enumerate(self.lines):
			self.group[index % self.bots] = np.append(self.group[index % self.bots], np.array([val]), axis = 0)

		print(self.group)


# 	def cal_cost(self, group[]):
# 		totaldist=0
# 		dist=0
# 		startpose[]=[0,0]
# 		endpose[]=[0,0]
# 		#right now its 3 seperate lines ,will change it for connected lines 
# 		for i in range(0,3):
# 			startpose[]=group[i][0]
# 			endpose[]=group[i][1]
# 			dist=math.sqrt( (endpose[0]-startpose[0])**2 + (endpose[1]-startpose[1])**2 )
# 			totaldist=totaldist+dist

# 		return totaldist

# #initial pop will be like pop=[cost1,cost2,cost3]


# #Evaluation (can find the pop with bestcost and hence bestpop....Fitness check)
# 	def Eval(pop):

# 		cost1=cal_cost(group1)
# 		cost2=cal_cost(group2)
# 		cost3=cal_cost(group3)
# 		costs=[cost1,cost2,cost3]
# 		cost=max(costs)
# 		bestcost=cost
# 		if (cost<bestcost):
# 			bestcost=cost
# 			bestpop=pop

# 		return bestcost

# #Now apply genetic algorithm on this initial pop



# #GA


# 	def crossover(parents,offspring_size):
# 		offspring=np.empty(offspring_size)	#initialise 
# 		crossover_pt=numpy.uint8(offspring_size[1]/2)

# 		for k in range(offspring_size[0]):
# 			parent1_id = k%parents.shape[0]
# 			parent2_id = (k+1)%parents.shape[0]
# 			offspring[k,0:crossover_pt]=parents[parent1_id,0:crossover_pt]
# 			offspring[k,crossover_pt]=parents[parent2_id,crossover_pt:]

# 		return offspring

# #adding variations to offspring using mutation
# 	def mutation(offspring):
# 		for id in range(offspring.shape[0]):

if __name__ == '__main__':
	lineSet = np.array([
				[(1,11), (11,1)],
				[(2,22), (22,2)],		
				[(3,33), (33,3)],
				[(4,44), (44,4)],
				[(5,55), (55,5)]
				])

	test = kimLee(bots = 3, lines = lineSet)




