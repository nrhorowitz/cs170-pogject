from random import randint
import random
from pointToIndices import costOfPoints
#an object represents each vertex in original graph
class Point:
    """A simple example class"""
    def __init__(self, label, adjacentVertices, rawLabel):
        self.rawLabel = rawLabel
        self.label = label
        self.adjacentVertices = adjacentVertices
#an object representing a point in the path
class pathPoint:
    def __init__(self, point, dropoffs, copyPoint=False):
        if copyPoint:
            self.rawLabel = copyPoint.rawLabel
            self.label = copyPoint.label
            self.adjacentVertices = copyPoint.adjacentVertices
            self.dropoffs = copyPoint.dropoffs
        else:
            self.rawLabel = point.rawLabel
            #int labeling graph vertices from 0 to |V| - 1
            self.label = point.label
            #list of vertices that this vertex has an edge to in the original graph LIST OF LABELS
            self.adjacentVertices = point.adjacentVertices
            #list of destinations for people dropped off here [cory, dwinelle] LIST OF LABELS
            self.dropoffs = dropoffs

#path is list of pathPoints in order of the path. points is a list of points that represent the graph
def cost(path, adjacencyMatrix):
    return costOfPoints(path, adjacencyMatrix)
#currdropoffs is a dictionary that is dropoff label to index in path
def simulatedAnnealing(path, points, iters, currdropoffs, adjacencyMatrix):
    choice = randint(0, 10)
    #add a random vertex before place
    coolingRate = .9
    stopTemp = .0001
    temp = 1
    currCost = cost(path, adjacencyMatrix)
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
                currPath[place] = pathPoint(currPath[place], [], True)
                currPath[place + 1] = pathPoint(currPath[place + 1], [], True)
                currPath[place - 1] = pathPoint(currPath[place - 1], [], True)
                if(tempPoint.dropoffs):
                    for i in tempPoint.dropoffs:
                        destination = randInt[0,1]
                        if destination:

                            path[place + 1].dropoffs.append(i)
                            currdropoffs[i] = place + 1
                        else:
                            path[place - 1].dropoffs.append(i)
                            currdropoffs[i] = place - 1
                path = path[:place] + path[place + 1:]
        else:
            randdropoff = currdropoffs.keys()[randint(0, len(currdropoffs) - 1)]
            destination = randInt[0,1]
            place = currdropoffs[randdropoff]
            currPath[place] = pathPoint(currPath[place], [], True)
            if destination:
                if (place != len(path) - 1):
                    currPath[place + 1] = pathPoint(currPath[place + 1], [], True)
                    path[place + 1].dropoffs.append(i)
                    currdropoffs[randdropoff] = place + 1
            else:
                if (currdropoffs[randdropoff] != 0:
                    currPath[place - 1] = pathPoint(currPath[place - 1], [], True)
                    path[place - 1].dropoffs.append(i)
                    currdropoffs[randdropoff] = place - 1
        newCost = cost(path, adjacencyMatrix)
        if (newCost < currCost):
            currCost = newCost
        else:
            rand = random.random()
            if rand < math.exp((newCost - currCost)/temp):
                currCost = newCost
            else:
                path = currPath
        temp = temp * coolingRate
    
        


            
        











