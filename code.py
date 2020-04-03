import numpy as np
import math
import numpy as np
import math
class kimLee():
     def __init__(self, bots, lines, botpos):
             self.lines = lines
             self.numLines = np.shape(self.lines)[0]
             self.bots = bots
             self.botspos=np.empty((0, 1, 2), float)
             self.group = np.empty((0, 2, 2), float)
             self.group = [self.group for i in range(self.bots)]
             for index, val in enumerate(self.lines):
                     self.group[index % self.bots] = np.append(self.group[index % self.bots], np.array([val]), axis = 0)
             print(self.group)
     def cal_cost(self,group,groupnum):
             oldend = botpos[groupnum]
             print("initial botpos:")
             print(oldend)
             grp=group[groupnum]
             totaldist = 0
             dist2 =  0
             p=1
             startpose = np.array([0,0])
             endpose = np.array([0,0])
             dtemp2 = 999999
             print("group size and group:")
             print(len(grp))
             print(grp)
             #print(oldend)
             while (p<=len(grp)):
                for x in range(0,len(grp)):
                             for y in range(0,2):
                                     nextpose = grp[x][y]
                                     #print(nextpose)
                                     dist2 = math.sqrt( (nextpose[0]-oldend[0])**2 + (nextpose[1]-oldend[1])**2 )
                                     if (dist2<dtemp2 ):
                                         dtemp2=dist2
                                         r=x
                                         s=y
                                         totaldist=totaldist+dtemp2+math.sqrt( (grp[x][0][0]-grp[x][1][0])**2 + (grp[x][0][1]-grp[x][1][1])**2 )
                #print(grp)
                #print(p)
                sn= int(not s)
                oldend=grp[r][sn]
                oldend2=grp[r][s]
                print("nearest line point")
                print(oldend2)
                print("other end of the same line")
                print(oldend)
                p=p+1
             return totaldist

	 def Eval(pop):
	 		 for j in pop:
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
     botpos = np.array([(0,1), (1,2), (2,3)])
     test = kimLee(bots = 3, lines = lineSet,botpos = botpos)
     grp = test.group
     calcost = test.cal_cost(grp,1)
     print(calcost)