from random import randint
#an object represents each vertex in original graph
class Point:
    """A simple example class"""
    def __init__(self, label, adjacentVertices):
        self.label = label
        self.adjacentVertices = adjacentVertices
#an object representing a point in the path
class pathPoint:
    def __init__(point, dropoffs):
        #int labeling graph vertices from 0 to |V| - 1
        self.label = point.label
        #list of vertices that this vertex has an edge to in the original graph LIST OF LABELS
        self.adjacentVertices = point.adjacentVertices
        #list of destinations for people dropped off here [cory, dwinelle] LIST OF LABELS
        self.dropOffs = dropOffs

#path is list of pathPoints in order of the path. points is a list of points that represent the graph
[soda]
def simulatedAnnealing(path, points, iters):
    choice = randint(0, 10)
    #add a random vertex before place
    for _ in range(iters):
        currPath = path
        if (choice >= 7):
            pointToAdd = points[randint(0, len(points) - 1)]
            pointToAdd = pathPoint(pointToAdd, [])
            place = randint(1, len(path) - 1)
            if (path[place - 1].label in pointToAdd.adjacentVertices):
                if (place == len(path - 1) or path[place + 1].label in pointToAdd.adjacentVertices):
                    path = path[0:place] + [pointToAdd] + path[place:]
        #remove a vertex
        if (choice >= 4):
            place = randint(1, len(path) - 2)
            tempPoint = path[place]
            if (path[place - 1].label in path[place + 1].adjacentVertices):
                if(tempPoint.dropOffs):
                    for i in tempPoint.dropOffs:
                        destination = randInt[0,1]
                        if destination:
                            path[place + 1].dropoffs.append(i)
                        else:
                            path[place - 1].dropoffs.append(i)
                path = path[:place] + path[place + 1:]
        else:











        