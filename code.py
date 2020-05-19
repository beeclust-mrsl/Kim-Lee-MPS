import numpy as np
import math
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10**6) 

class kimLee():
	def __init__(self, numBots, lines, pose):
		self.lines = lines
		self.numlines = np.shape(self.lines)[0]
		self.bots = numBots
		self.pose = pose
		
		self.population = []
		
		self.bestPop = []       #used to store all 'best population'
		self.bestPop_cost = []  #and their costs
		self.iteration = 0	#keeps a count of generation
		self.gen = 100          #number of generation
		
		#plotting
		self.piterations = []
		
		#To return to main
		self.final_best_pop = 0
		self.final_best_cost = 0
		self.final_line = []
	
	def initPop(self):
		pop_size  = 4
		self.population = np.random.random_integers(low = 0, high = self.bots-1, size = (pop_size, self.numlines))

		if self.iteration == 0:
			print('Original Population:\n',self.population)
	
	def groupGenes(self, pos_sol):
		groups = []
		
		for i in range(self.bots):
			line_index = 0
			val = []
			for bot_index in pos_sol:
				if i == bot_index:
					val.append(self.lines[line_index])
				line_index = line_index + 1
			groups.append(val)
		return groups
	
	def nextDist(self, pose, line, chpose):
		x0 = pose[0]
		y0 = pose[1]
		x1 = line[0][0]
		y1 = line[0][1]
		x2 = line[1][0]
		y2 = line[1][1]

		d1 = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)
		d2 = math.sqrt((x2 - x0)**2 + (y2 - y0)**2)
		
		if chpose == 1:
			if d1<d2:
				end = [x2,y2]
				start = [x1, y1]
				return start, end
			else:
				end = [x1, y1]
				start = [x2, y2]
				return start, end
		dist = min(d1,d2)
		return dist
	
	def nextline(self, pose, group, bot_index, line = []):
		dist = []
		for pts in group:
			distbtw = self.nextDist(pose = pose[bot_index], line =  pts, chpose = 0)
			dist.append(distbtw)  
			
		if len(dist) == 0:
			p = list(pose[bot_index])
			line.append(p)
			return line
		
		elif len(dist) == 1:
			if (len(line) == 0):
				p = list(pose[bot_index])
				line.append(p)
			idx = 0 
			start, end = self.nextDist(pose = pose[bot_index], line = group[idx], chpose = 1)
			line.append(start)
			line.append(end)
			return line
		
		else:
			if (len(line) == 0):
				p = list((pose[bot_index]))
				line.append(p)
				
				idx = dist.index(min(dist))
				start, end = self.nextDist(pose = pose[bot_index], line = group[idx], chpose = 1)
				line.append(start)
				line.append(end)
				
				pose[bot_index] = end
				group.remove(group[idx])
				line1 = self.nextline(pose, group, bot_index, line)
				return line
	
	def groupDist(self, line):
		cost = 0
		for index in range(len(line) - 1):
			pt1 = line[index]
			pt2 = line[index+1]
			dist = math.sqrt( ((pt1[0] - pt2[0])**2)+((pt1[1] - pt2[1])**2) )
			cost = cost + dist
		return cost
	
	def groupCost(self, groupscost):
		maxCost = max(groupscost)
		return maxCost
	
	def evaluate(self, fitness):
		best = min(fitness)
		best_idx = fitness.index(best)
		
		self.bestPop.append(self.population[best_idx])
		self.bestPop_cost.append(best)
		
	def select_parents(self, fitness):
		num_parents = int(len(self.population)/2)
		parents = np.empty((num_parents, self.population.shape[1]))
		
		for pn in range(num_parents):
			max_fitness_idx = np.where(fitness == np.min(fitness))
			max_fitness_idx = int(max_fitness_idx[0][0])
			parents[pn, :] = self.population[max_fitness_idx, :]
			fitness[max_fitness_idx] = 999999999999
		return parents
	
	def crossover(self, parents):
		pop_size = len(self.population)
		offspring_size = (pop_size - parents.shape[0], parents.shape[1])
		offspring = np.empty(offspring_size)
		
		#2 point crossover
		crossover_point1 = np.uint8(offspring_size[1]/3)
		crossover_point2 = np.uint8((2*offspring_size[1])/3)
		
		for k in range(offspring_size[0]):
			parent1_idx = k%parents.shape[0]
			parent2_idx = (k+1)%parents.shape[0]
			
			offspring[k, 0:crossover_point1] = parents[parent1_idx, 0:crossover_point1]
			offspring[k, crossover_point2:] = parents[parent1_idx, crossover_point2:]
			offspring[k, crossover_point1:crossover_point2] = parents[parent2_idx, crossover_point1:crossover_point2]
		return offspring
	
	def mutation (self, offspring):  
		#Reciprocal exchange
		number = offspring.shape[1]
		
		for pop in offspring:
			idx1 = np.random.random_integers(0, number-1) 
			idx2 = np.random.random_integers(0, number-1)
			
			while idx1 == idx2:
				idx2 = np.random.random_integers(0, number-1)
			
			temp = pop[idx1]
			pop[idx1] = pop[idx2]
			pop[idx2] = temp
		return offspring
	
	def main(self):
		if (len(self.population) == 0):
			self.initPop()  
			const_pose = list(self.pose)
			fitness = []				# To store costs for individuals
			
			for pos_sol in self.population:
				pose = np.array(const_pose)	#initial pose should remain the same
				groups = self.groupGenes(pos_sol)  #Divides into groups
				
				groupscost = []
				bot_index = 0
				for group in groups:
					line = self.nextline(pose, group, bot_index, line = [])	#path to be followed
					bot_index = bot_index + 1
					c = self.groupDist(line)	#Cost for the path
					groupscost.append(c)
					maxCost = self.groupCost(groupscost)	#Max cost of the group/Final cost
					fitness.append(maxCost)			#fitness of the individual
				
				self.evaluate(fitness)				#Select and store best population
				self.piterations.append(self.iteration)		#for plotting
				
				if self.iteration == 0:
					try:
						self.gen = int(input('Enter No. of generations (default 100): '))	#Change number of generation
					except:
						self.gen = 100
				
				if self.iteration < self.gen:
					parents = self.select_parents(fitness = fitness)			#Select fittest individuals
					offspring_crossover = self.crossover(parents)				#2 point crossover
					offspring_mutation = self.mutation(offspring = offspring_crossover)	#Reciprocal Exchange Mutation
					
					self.population = []		#Reset for new population
					
					for parent in parents:
						parent = list(parent)
						self.population.append(parent)	# Fit individuals from last population
					for new_pop in offspring_mutation:
						new_pop = list(new_pop)
						self.population.append(new_pop)	#Mutated/new individuals
						
					self.population = np.array(self.population)
					self.iteration = self.iteration + 1
					self.main()				#Recursive call
				else:
					idx =  self.bestPop_cost.index(min(self.bestPop_cost))
					self.final_best_pop = self.bestPop[idx]
					self.final_best_cost = self.bestPop_cost[idx]
					
					#GETTING RELEVANT DATA: FINAL POPULATION
					print ('\nFinal Best Population: ', self.final_best_pop, '\nCost:', self.final_best_cost)
					pose = self.pose
					groups = self.groupGenes(final_best_pop)
					
					print('')
					groupscost = []
					bot_index = 0
					for group in groups:
						line = self.nextline(pose, group, bot_index, line = [])
						bot_index = bot_index + 1
						
						print ('line',bot_index,line)
						
						self.final_line.append(line)
						c = self.groupDist(line)
						groupscost.append(c)
					
					print ('\nGroup wise Cost\n',groupscost)
					
					plt.plot(self.piterations, self.bestPop_cost, 'b-')
					plt.xlabel('X axis')
					plt.ylabel('Y axis')
					plt.show()

class visualizer():
	def __init__(self, lines):
		self.x_pts = []
		self.y_pts = []
		
		self.fig = plt.figure()
		self.lines = lines 
		
	def plot(self, p1):
		idx = 0
		clrs = ['b-', 'g-', 'r-', 'c-', 'm-', 'y-', 'k-', 'w-']
		mark_pts = ['bo', 'go', 'ro', 'co', 'mo', 'yo', 'ko', 'wo']
		
		for line in self.lines:
			x = list(line[i][0] for i in range(len(line)))
			y = list(line[i][1] for i in range(len(line)))
			
			p1.plot(x, y, clrs[idx])
			p1.plot(x, y, mark_pts[idx])
			
			idx = idx + 1
			if (idx == len(clrs)):
				idx = 0
		#plt.show()
	
	def points_on_line(self):
		for line in self.lines:
			lx = []
			ly = []
			for index in range(len(line) - 1):
				pt1 = line[index]
				pt2 = line[index+1]
				
				x1 = pt1[0]
				y1 = pt1[1]
				x2 = pt2[0]
				y2 = pt2[1]
				
				num_btw = 3*int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))	#Number of points btw 2 points
				for t in range(num_btw):
					x = x1 + (x2-x1) * (1/num_btw) * t
					y = y1 + (y2-y1) * (1/num_btw) * t
					
					lx.append(x)
					ly.append(y)
			
			self.x_pts.append(lx)
			self.y_pts.append(ly)
	
	def animation(self):
		mark_pts = ['bo', 'go', 'ro', 'co', 'mo', 'yo', 'ko', 'wo']
		idx = 0
		Anim = []
		p1 = self.fig.add_subplot(111)
		self.plot(p1)
		
		def next(index):
			color_id = index
			
			if (color_id+1 == len(mark_pts)):
				color_id = 5
			
			pt, = p1.plot([], [], mark_pts[color_id+1])
			
			def bot():
				i = 0
				while(True):
					yield i
					i += 1
			def run(c):
				pt.set_data(self.x_pts[index][c], self.y_pts[index][c])
			
			Anim.append(animation.FuncAnimation(self.fig,run,bot,interval=1))
			
			if index == len(self.x_pts) :
				plt.show()
			else:
				index = index + 1
				next(index) #Recursive Function as a loop
		
		next(index = -1)
	'''	
	def visualizer(self):
	'''	
	def main(self):
		#self.plot()
		self.points_on_line()
		self.animation()
		

if __name__ == '__main__':
	#Array of lines to be printed. Format: [(start_x, start_y), (end_x, end_y)]
	lineSet = np.array([
		[(1,11), (11,1)],
		[(2,22), (22,2)],
		[(3,33), (33,3)],
		[(4,44), (44,4)],
		[(5,55), (55,5)],
	])
	
	#Initial position of each robot
	pose = np.array([(0,1), (1,2), (2,3)])
	test = kimLee(numBots = pose.shape[0], lines = lineSet, pose = pose)
	test.main()
	
	display = visualizer(lines = test.final_line)
	display.main()
