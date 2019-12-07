"""
simulatedAnnealing() takes in path, which is a list of pathPoints, points, which is a list of Points, currdropoffs, which is a dictionary that maps
a ta home index to the pathPoint. so if someone living in index 0, and was dropped off at index 3 of the path, it would contain
the mapping 0:3
it then changes path to be the calculated optimum. No return
adjacencyMatrix is an adjacency matrix of the graph 
#avg edge weight is the averageedgeweight of the graph
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
def cost(path, adjacencyMatrix, final = False):
    return costOfPoints(path, adjacencyMatrix, final)
#currdropoffs is a dictionary that is dropoff label to index in path
def simulatedAnnealing(path, points, currdropoffs, adjacencyMatrix, avgEdgeWeight = 0):
    
    
    coolingRate = .9999
    stopTemp = -avgEdgeWeight[0] / math.log(.1)
    temp = -avgEdgeWeight[2]/math.log(.8)
    worstChange, minChange = 0, float("-inf")
    currCost = cost(path, adjacencyMatrix)
    optimumdropoff = deepcopy(currdropoffs)
    optimumCost =  currCost
    optimumPath = deepcopy(path)
    
    print("Soda Sol:", currCost)
    while(temp > stopTemp):
        print(currCost)
        for i in path:
            print(i.label, end = " ")
        print()
        choice = randint(0, 1000)
        currPath = path[:]
        currdropoffsDict = deepcopy(currdropoffs)
        
        #add a random vertex before place
        if (choice >= 450):
            # print("adding")
            place = randint(1, len(path) - 1)
            pointToAdd = points[random.choice(path[place - 1].adjacentVertices)]
            
            pointToAdd = pathPoint(pointToAdd, [])
            chance = randint(0, 10)
            # print(path[place - 1].adjacentVertices, random.choice(path[place - 1].adjacentVertices), path[place - 1].adjacentVertices, place, chance, pointToAdd.adjacentVertices)
            if (chance > 3):
                if (path[place - 1].label in pointToAdd.adjacentVertices and path[place].label in pointToAdd.adjacentVertices):
                    # print(pointToAdd.label, place)
                    # print("adding vertex\n")
                    for i in currdropoffs.keys():
                        if currdropoffs[i] >= place:
                            currdropoffs[i] +=1
                    path = path[0:place] + [pointToAdd] + path[place:]
                    # print("updated")
                    # for i in path:
                    #     print(i.label, sep = '')
                    
                   
            else:
                if (path[place - 1].label in pointToAdd.adjacentVertices and path[place - 1].label != path[place].label ):
                    prevCopy = pathPoint(points[(path[place - 1].label)], [])
                    for i in currdropoffs.keys():
                        if currdropoffs[i] >= place:
                            currdropoffs[i] +=2
                    path = path[0:place] + [pointToAdd] + [prevCopy] + path[place:]
                    
                    # print("\n")
        #remove vertices
        elif (choice > 350 and len(path) >= 3):
            place = randint(1, len(path) - 2)
            numRemove = randint(1, len(path) // 3)
            if len(path) - 1 - place < numRemove:
                numRemove = randint(1, len(path) - 1 - place)
            print(place, numRemove, "removedata", len(path))
            if (path[place - 1].label in path[place + numRemove].adjacentVertices or path[place - 1].label == path[place + numRemove].label):
                # print("removing vertex\n")
                currPath[place] = pathPoint(currPath[place], [], True)
                currPath[place + numRemove] = pathPoint(currPath[place + numRemove], [], True)
                currPath[place - 1] = pathPoint(currPath[place - 1], [], True)
                if place > 2:
                    currPath[place - 2] = pathPoint(currPath[place - 2], [], True)
                lostdropoffs = []
                for i in range(place, place + numRemove):
                    lostdropoffs += path[i].dropoffs
                if(lostdropoffs):
                    for i in lostdropoffs:
                        destination = randint(0,1)
                        # print(destination , place+numRemove != len(path) - 1)
                        if destination and place+numRemove != len(path) - 1:
                            path[place + numRemove].dropoffs.add(i)
                            currdropoffs[i] = place + numRemove
                            # print(i, "was moved to",place + + numRemove, path[place].dropoffs)
                        else:
                            path[place - 1].dropoffs.add(i)
                            currdropoffs[i] = place - 1
                            # print(i, "was moved to", place - 1)
                for i in currdropoffs.keys():
                        if currdropoffs[i] >= place + numRemove:
                            currdropoffs[i] -=numRemove
                path = path[:place] + path[place + numRemove:]
                #merging two points into one if they are adjacent and equal
                place -= 1
                # for i in path:
                    # print(list(i.dropoffs), i.label)
                if (path[place].label == path[place + 1].label and len(path) > 2):
                    currPath[place] = pathPoint(currPath[place], [], True)
                    currPath[place + 1] = pathPoint(currPath[place + 1], [], True)
                    for i in path[place + 1].dropoffs:
                        path[place].dropoffs.add(i)
                        currdropoffs[i] -=1
                    for i in currdropoffs.keys():
                        if currdropoffs[i] > place:
                            currdropoffs[i] -=1
                    path = path[:place + 1] + path[place + 2:]
                    #if they merged onto last point
                    if (place == len(path) - 1):
                        for i in path[place].dropoffs:
                            path[place - 1].dropoffs.add(i)
                            currdropoffs[i] -=1
                        path[place].dropoffs = set()
        elif (choice > 349):
            if randint(0, 8) == 2:
                currdropoffs = deepcopy(optimumdropoff)
                currCost = optimumCost
                path = deepcopy(optimumPath)
        else:
            # print("moving DropOff\n")
            randdropoff = list(currdropoffs.keys())[randint(0, len(currdropoffs) - 1)]
            destination = randint(0, len(path) - 2)
            place = currdropoffs[randdropoff]
            # print(place, currdropoffs)
            currPath[place] = pathPoint(currPath[place], [], True)
            currPath[destination] = pathPoint(currPath[destination], [], True)
            path[place].dropoffs.remove(randdropoff)
            path[destination].dropoffs.add(randdropoff)
            currdropoffs[randdropoff] = destination
            
            # print(destination, randdropoff, place, currdropoffs)
            # for i in range(len(path)):
            #     print(list(path[i].dropoffs), i) 
            
            
            # if destination:

            #     if (place < len(path) - 2):
            #         for i in range(len(path)):
            #             print(list(path[i].dropoffs), i)
            #         print(place, list(path[place].dropoffs), "dropoffs1", list(path[place + 1].dropoffs), randdropoff, currdropoffs)
            #         currPath[place + 1] = pathPoint(currPath[place + 1], [], True)
            #         path[place + 1].dropoffs.add(randdropoff) 
            #         path[place].dropoffs.remove(randdropoff)
            #         currdropoffs[randdropoff] = place + 1
            #         # print(place, list(path[place].dropoffs),list(path[place + 1].dropoffs), "dropoffs2", randdropoff, currdropoffs)
            #         # for i in range(len(path)):
            #         #     print(list(path[i].dropoffs), i)
            # else:
            #     if (place != 0):
            #         for i in range(len(path)):
            #             print(list(path[i].dropoffs), i)
            #         print(place, list(path[place].dropoffs), "dropoffs3", list(path[place - 1].dropoffs), randdropoff, currdropoffs)
            #         currPath[place - 1] = pathPoint(currPath[place - 1], [], True)
            #         path[place - 1].dropoffs.add(randdropoff)
            #         path[place].dropoffs.remove(randdropoff)
            #         currdropoffs[randdropoff] = place - 1
            #         # print(place, list(path[place].dropoffs),list(path[place - 1].dropoffs), "dropoffs4", randdropoff, currdropoffs)
            #         # for i in range(len(path)):
            #         #     print(list(path[i].dropoffs), i)
        newCost = cost(path, adjacencyMatrix)
        # print(newCost, currdropoffs)
        # for i in path:
        #     print(i.label, end = ' ')
        # for i in range(len(path)):
        #     print(list(path[i].dropoffs), i)
        # print()
        
        if newCost <= optimumCost:
            optimumdropoff = deepcopy(currdropoffs)
            optimumCost =  newCost
            optimumPath = deepcopy(path)
        elif (newCost <= currCost):
            currCost = newCost
            # print("taken")
        else:
            rand = random.random()
            # print(currCost, newCost, "costs")
            if (worstChange > currCost - newCost):
                worstChange = currCost - newCost
            if minChange < currCost - newCost:
                minChange = currCost - newCost
            if rand < math.exp(-(newCost - currCost)/temp):
                # print("temps", "Delta:", (newCost - currCost), "Temperature:", (temp), "rand:", rand, "prob:", math.exp(-float(newCost - currCost)/(temp)))
                # print("taken")
                currCost = newCost
                # for i in range(len(path)):
                #     print(list(path[i].dropoffs), i)
            else:
                # print("not")
                path = currPath
                currdropoffs = currdropoffsDict
        
        temp = temp * coolingRate
        # sumError = 0
        # for i in path:
        #     sumError += len(i.dropoffs)
        #     if(sumError >4):
        #         # print("HOLUP")
        #         # print(currdropoffs)
        #         for i in path:
        #             print(list(i.dropoffs), i.label)
        #         exit()
        # for i in currdropoffs.keys():
        #     if (i not in path[currdropoffs[i]].dropoffs):
        #         print("HOLUP")
        #         print(list(sumHomes))
        #         print(currdropoffs)
        #         for i in path:
        #             print(list(i.dropoffs), i.label)

        #         exit()   
    cost(optimumPath, adjacencyMatrix, True)
    print("final Solution Cost:", optimumCost)
    # for i in range(len(optimumPath)):
        # print(list(optimumPath[i].dropoffs), i)
    return optimumPath

    
        


            
