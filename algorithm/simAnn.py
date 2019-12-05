from random import randint
class Point:
    """A simple example class"""
    def __init__(self, label, adjacentVertices):
        self.label = label
        #list of points
        self.adjacentVertices = adjacentVertices
class pathPoint:
    def __init__(point, dropoffs):
        self.label = point.label
        self.adjacentVertices = point.adjacentVertices
        self.dropOffs = dropOffs

        #path is list of points in order of the path. points is a list of points that repres
    def simulatedAnnealing(path, points):
        choice = randint(0, 10)
        #add a random vertex
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
                path = path[:place] + path[place + 1:]
            if(tempPoint.dropOffs):
                for i in tempPoint.dropOffs
        else:






        