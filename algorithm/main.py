<<<<<<< HEAD
MAX_VALUE = float('inf')

# Given file name, return input in data form
def read_input(file_name):
    f = open("inputs/" + file_name, "r")
    contents = f.readlines()
    data = []
    for i in range(5, 5 + int(contents[0])):
        d = contents[i].split(" ")
        row = []
        for val in d:
            if val == 'x':
                row.append(MAX_VALUE)
            elif '\n' in val:
                v = val[:len(val)-1]
                if v == 'x':
                    row.append(MAX_VALUE)
                else:
                    row.append(int(v))
            else:
                row.append(int(val))
        data.append(row)
    print(data)
    
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
=======
from simAnn import Point
from simAnn import pathPoint

MAX_VALUE = float('inf')

# Given file name, return input in data form
# convert input to null path and list of points and distance lookup
# returns list of points, global lookup for distance between points
def read_input(file_name):
    f = open("inputs/" + file_name, "r")
    contents = f.readlines()
    labelLookup = contents[2].split(" ")
    labelLookup[len(labelLookup) - 1] = labelLookup[len(labelLookup) - 1][:len(labelLookup[len(labelLookup) - 1]) - 1]
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
        globalLookup.append(globalLookupRow)
        p = Point(i - 5, adjacentList, labelLookup[i - 5])
        listOfPoints.append(p)
    return listOfPoints, globalLookup

def run_solver():
    return 0

# Given list of path points, generate output file with name
def generate_output(listOfPathPoints, name):
    return 0

def sweep_inputs():
    # try every input, 
    # read_input ---> list of points, global distance lookup
    # start with some guess ****** pathpoint
    # run_solver on list of pathpoints ---> the correct list of pathpoints
    # generate_output correct list of pathpoint ---> .out
    return 0
>>>>>>> 20defb23d7d62e86b5f05f509652f83fff341440
