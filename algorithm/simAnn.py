from random import randint
import random
from math import e
#an object represents each vertex in original graph
class Point:
    """A simple example class"""
    def __init__(self, label, adjacentVertices, rawLabel):
        self.rawLabel = rawLabel
        self.label = label
        self.adjacentVertices = adjacentVertices
#an object representing a point in the path
class pathPoint:
    def __init__(point, dropoffs):
        self.rawLabel = rawLabel
        #int labeling graph vertices from 0 to |V| - 1
        self.label = point.label
        #list of vertices that this vertex has an edge to in the original graph LIST OF LABELS
        self.adjacentVertices = point.adjacentVertices
        #list of destinations for people dropped off here [cory, dwinelle] LIST OF LABELS
        self.dropOffs = dropOffs

#path is list of pathPoints in order of the path. points is a list of points that represent the graph
def cost():
    return 0
#currDropoffs is a dictionary that is dropOff label to index in path
def simulatedAnnealing(path, points, iters, currDropOffs):
    choice = randint(0, 10)
    #add a random vertex before place
    coolingRate = .9
    stopTemp = .0001
    temp = 1
    currCost = cost(path)
    while(temp > stopTemp):
        currPath = path[:]
        if (choice >= 8):
            pointToAdd = points[randint(0, len(points) - 1)]
            pointToAdd = pathPoint(pointToAdd, [])
            place = randint(1, len(path) - 1)
            if (path[place - 1].label in pointToAdd.adjacentVertices):
                if (place == len(path - 1) or path[place + 1].label in pointToAdd.adjacentVertices):
                    path = path[0:place] + [pointToAdd] + path[place:]
        #remove a vertex
        if (choice >= 6 and len(path) >= 3):
            place = randint(1, len(path) - 2)
            tempPoint = path[place]
            if (path[place - 1].label in path[place + 1].adjacentVertices):
                if(tempPoint.dropOffs):
                    for i in tempPoint.dropOffs:
                        destination = randInt[0,1]
                        if destination:
                            path[place + 1].dropoffs.append(i)
                            currDropOffs[i] = place + 1
                        else:
                            path[place - 1].dropoffs.append(i)
                            currDropOffs[i] = place - 1
                path = path[:place] + path[place + 1:]
        else:
            randDropOff = currDropOffs.keys()[randint(0, len(currDropoffs) - 1)]
            destination = randInt[0,1]
            if destination:
                if (currDropOffs[randDropOff] != len(path) - 1):
                    path[currDropOffs[randDropOff] + 1].dropoffs.append(i)
                    currDropOffs[randDropOff] = currDropOffs[randDropOff] + 1
            else:
                if (currDropOffs[randDropOff] != 0:
                    path[currDropOffs[randDropOff] - 1].dropoffs.append(i)
                    currDropOffs[randDropOff] = currDropOffs[randDropOff] - 1
        newCost = cost(path)
        if (newCost < currCost):
            currCost = newCost
        else:
            rand = random.random()
            if rand < math.exp((newCost - currCost)/temp):
                currCost = newCost
            else:
                path = currPath
        temp = temp * coolingRate
    
        


            
        











