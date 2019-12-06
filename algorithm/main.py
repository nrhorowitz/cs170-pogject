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
                globalLookupRow.append('x')
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
