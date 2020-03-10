#5 lines represented by their start pose and end pose
lines=[
		[ [x1,y1] , [xn1,yn1] ],
		[ [x2,y2] , [xn2,yn2] ],		
		[ [x3,y3] , [xn3,yn3] ],
		[ [x4,y4] , [xn4,yn4] ],
		[ [x5,y5] , [xn5,yn5] ]

		]

#we have only 3 bots


#making population and selecting best population using genetic algorithm
#now cost of these lines will act as weights so we will arrange these weights(costs) in group of three lines for 
#let initial pop has three chromosomes as array of three cost in pattern (1,2,3)  (2,3,4)   (3,4,5) according to 3 bots 


group1[]=[ [ [x1,y1] , [xn1,yn1] ],
			[ [x2,y2] , [xn2,yn2] ],		
			[ [x3,y3] , [xn3,yn3] ], ]

group2[]=[ [ [x2,y2] , [xn2,yn2] ],
			[ [x3,y3] , [xn3,yn3] ],		
			[ [x4,y4] , [xn4,yn4] ], ]

group3[]=[ [ [x3,y3] , [xn3,yn3] ],
			[ [x4,y4] , [xn4,yn4] ],		
			[ [x5,y5] , [xn5,yn5] ], ]



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


















def Fitness(inp,pop):
	fitness=numpy.sum(pop*inp,axis=1)
	return fitness

def MatingSelect(pop,fitness,Num_prt):
	parents
