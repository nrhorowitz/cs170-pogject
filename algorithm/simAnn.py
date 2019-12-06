"""
simulatedAnnealing() takes in path, which is a list of pathPoints, points, which is a list of Points, currdropoffs, which is a dictionary that maps
a ta home index to the pathPoint. so if someone living in index 0, and was dropped off at index 3 of the path, it would contain
the mapping 0:3
it then changes path to be the calculated optimum. No return
adjacencyMatrix is an adjacency matrix of the graph 
"""
from random import randint
import random
import math
from pointsToIndices import costOfPoints
from copy import deepcopy
#an object represents each vertex in original graph
class Point:
    def __init__(self, label, adjacentVertices, rawLabel):
        self.rawLabel = rawLabel
        self.label = label
        self.adjacentVertices = adjacentVertices
#an object representing a point in the path
class pathPoint:
    def __init__(self, point, dropoffs, copyPoint=False):
        if copyPoint:
            self.rawLabel = point.rawLabel
            self.label = point.label
            self.adjacentVertices = point.adjacentVertices
            self.dropoffs = set(point.dropoffs)
        else:
            self.rawLabel = point.rawLabel
            #int labeling graph vertices from 0 to |V| - 1
            self.label = point.label
            #list of vertices that this vertex has an edge to in the original graph LIST OF LABELS
            self.adjacentVertices = point.adjacentVertices
            #list of destinations for people dropped off here [cory, dwinelle]  SET OF LABELS
            self.dropoffs = set(dropoffs)

#path is list of pathPoints in order of the path. points is a list of points that represent the graph
def cost(path, adjacencyMatrix):
    return costOfPoints(path, adjacencyMatrix)
#currdropoffs is a dictionary that is dropoff label to index in path
def simulatedAnnealing(path, points, currdropoffs, adjacencyMatrix):
    
    
    coolingRate = .99
    stopTemp = 1
    temp = 200
    currCost = cost(path, adjacencyMatrix)
    while(temp > stopTemp):
        choice = randint(0, 10)
        currPath = path[:]
        currdropoffsDict = deepcopy(currdropoffs)
        #add a random vertex before place
        if (choice >= 3):
            print("adding")
            pointToAdd = points[randint(0, len(points) - 1)]
            pointToAdd = pathPoint(pointToAdd, [])
            place = randint(1, len(path) - 1)
            chance = randint(0, 10)
            if (chance > 2):
                if (path[place - 1].label in pointToAdd.adjacentVertices and path[place].label in pointToAdd.adjacentVertices):
                    # print(pointToAdd.label, place)
                    # print("adding vertex\n")
                    for i in currdropoffs.keys():
                        if currdropoffs[i] >= place:
                            currdropoffs[i] +=1
                    path = path[0:place] + [pointToAdd] + path[place:]
                   
            else:
                if (path[place - 1].label in pointToAdd.adjacentVertices and path[place - 1].label != path[place].label ):
                    prevCopy = pathPoint(points[(path[place - 1].label)], [])
                    for i in currdropoffs.keys():
                        if currdropoffs[i] >= place:
                            currdropoffs[i] +=2
                    path = path[0:place] + [pointToAdd] + [prevCopy] + path[place:]
                    # print("\n")
        #remove a vertex
        elif (choice >= 2 and len(path) >= 3):
            print("removing vertex\n")
            place = randint(1, len(path) - 2)
            tempPoint = path[place]
            if (path[place - 1].label in path[place + 1].adjacentVertices):
                currPath[place] = pathPoint(currPath[place], [], True)
                currPath[place + 1] = pathPoint(currPath[place + 1], [], True)
                currPath[place - 1] = pathPoint(currPath[place - 1], [], True)
                if(tempPoint.dropoffs):
                    for i in tempPoint.dropoffs:
                        destination = randint(0,1)
                        if destination:
                            path[place + 1].dropoffs.add(i)
                            # print(i, "was moved to",place + 1)
                        else:
                            path[place - 1].dropoffs.add(i)
                            currdropoffs[i] = place - 1
                            # print(i, place - 1)
                path = path[:place] + path[place + 1:]
        else:
            print("moving DropOff\n")
            randdropoff = list(currdropoffs.keys())[randint(0, len(currdropoffs) - 1)]
            destination = randint(0, 1)
            place = currdropoffs[randdropoff]
            currPath[place] = pathPoint(currPath[place], [], True)
            if destination:
                if (place < len(path) - 2):
                    # for i in range(len(path)):
                    #     print(list(path[i].dropoffs), i)
                    # print(place, list(path[place].dropoffs), "dropoffs1", list(path[place + 1].dropoffs), randdropoff, currdropoffs)
                    currPath[place + 1] = pathPoint(currPath[place + 1], [], True)
                    path[place + 1].dropoffs.add(randdropoff) 
                    path[place].dropoffs.remove(randdropoff)
                    currdropoffs[randdropoff] = place + 1
                    # print(place, list(path[place].dropoffs),list(path[place + 1].dropoffs), "dropoffs2", randdropoff, currdropoffs)
                    # for i in range(len(path)):
                    #     print(list(path[i].dropoffs), i)
            else:
                if (place != 0):
                    # for i in range(len(path)):
                    #     print(list(path[i].dropoffs), i)
                    # print(place, list(path[place].dropoffs), "dropoffs3", list(path[place - 1].dropoffs), randdropoff, currdropoffs)
                    currPath[place - 1] = pathPoint(currPath[place - 1], [], True)
                    path[place - 1].dropoffs.add(randdropoff)
                    path[place].dropoffs.remove(randdropoff)
                    currdropoffs[randdropoff] = place - 1
                    # print(place, list(path[place].dropoffs),list(path[place - 1].dropoffs), "dropoffs4", randdropoff, currdropoffs)
                    # for i in range(len(path)):
                    #     print(list(path[i].dropoffs), i)
        newCost = cost(path, adjacencyMatrix)
        if (newCost <= currCost):
            currCost = newCost
        else:
            rand = random.random()
            # print(currCost, newCost, "costs")
            # print("temps", (newCost - currCost), (temp), math.exp(-float(newCost - currCost)/(temp)), temp)
            if rand < math.exp(-(newCost - currCost)/temp):
                # print("taken")
                currCost = newCost
                # for i in range(len(path)):
                    # print(list(path[i].dropoffs), i)
            # else:
                # print("not")
                path = currPath
                currdropoffs = currdropoffsDict
        temp = temp * coolingRate
    # for i in path:
        # print(i.label)
    return path
    
        


            
