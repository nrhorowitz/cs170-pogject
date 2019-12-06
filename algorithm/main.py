from simAnn import Point
from simAnn import pathPoint

MAX_VALUE = float('inf')

# Given file name, return input in data form
# convert input to null path and list of points and distance lookup
def read_input(file_name):
    f = open("inputs/" + file_name, "r")
    contents = f.readlines()
    labelLookup = contents[2].split(" ")
    labelLookup[len(labelLookup) - 1] = labelLookup[len(labelLookup) - 1][:len(labelLookup[len(labelLookup) - 1]) - 1]
    # print(labelLookup)
    listOfPoints = []
    globalLookup = []
    for i in range(5, 5 + int(contents[0])):
        adjacentList = []
        d = contents[i].split(" ")
        globalLookupRow = []
        for j in range(0, int(contents[0])):
            if 'x' not in d[j]:
                if '\n' in d[j]:
                    globalLookupRow.append(int(d[j][:len(d[j])-1]))
                else:
                    globalLookupRow.append(int(d[j]))
                adjacentList.append(j)
            else:
                globalLookupRow.append(MAX_VALUE)
        print(adjacentList)
        globalLookup.append(globalLookupRow)
        p = Point(i - 5, adjacentList, labelLookup[i - 5])
        listOfPoints.append(p)
    print(globalLookup)
    
    return 0

# Given table, return shortest path and distance between any two vertices
def shortest_path_any_two(input):
    return 0

# Return total energy expended, if TA cannot get home return float('inf')
def path_cost(input, path):
    return 0

# Add a random vertex to a random part of the path
# TODO: probably should be close by
def add_vertex(input, path):
    return 0

# Remove a random vertex from the path
def remove_vertex(input, path):
    return 0

# Dropoff point 
def change_dropoff(input, path):
    c = 3
    return 0
