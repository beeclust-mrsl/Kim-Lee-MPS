import numpy as np
import math

class GA:
#5 lines represented by their start pose and end pose
	lines=np.array([
			[ [x1,y1] , [xn1,yn1] ],
			[ [x2,y2] , [xn2,yn2] ],		
			[ [x3,y3] , [xn3,yn3] ],
			[ [x4,y4] , [xn4,yn4] ],
			[ [x5,y5] , [xn5,yn5] ]
			])

#we have only 3 bots


#making population and selecting best population using genetic algorithm
#now cost of these lines will act as weights so we will arrange these weights(costs) in group of three lines for 
#let initial pop has three chromosomes as array of three cost in pattern (1,2,3)  (2,3,4)   (3,4,5) according to 3 bots 


	group1[]=np.array([ lines[0]	, lines[1] , lines[2] ]	)	
			
	group2[]=np.array([ lines[1]	, lines[2] , lines[3] ] )

	group3[]=np.array([ lines[2]	, lines[3] , lines[4] ] )



	def cal_cost(group[]):
		totaldist=0
		dist=0
		startpose[]=[0,0]
		endpose[]=[0,0]
	#right now its 3 seperate lines ,will change it for connected lines 
		for i in range(0,3):
			startpose[]=group[i][0]
			endpose[]=group[i][1]
			dist=math.sqrt( (endpose[0]-startpose[0])**2 + (endpose[1]-startpose[1])**2 )
			totaldist=totaldist+dist

		return totaldist

#initial pop will be like pop=[cost1,cost2,cost3]


#Evaluation (can find the pop with bestcost and hence bestpop....Fitness check)
	def Eval(pop):

		cost1=cal_cost(group1)
		cost2=cal_cost(group2)
		cost3=cal_cost(group3)
		costs=[cost1,cost2,cost3]
		cost=max(costs)
		bestcost=cost
		if (cost<bestcost):
			bestcost=cost
			bestpop=pop

		return bestcost

#Now apply genetic algorithm on this initial pop



#GA


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
		for id in range(offspring.shape[0]):




