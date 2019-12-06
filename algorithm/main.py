from simAnn import Point
from simAnn import pathPoint
from simAnn import simulatedAnnealing

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
    labelToIndex = {}
    for i in range(len(labelLookup)):
        labelToIndex[labelLookup[i]] = i
    start = contents[4][:len(contents[4])-1]
    homeIndex = labelToIndex[start]
    defaultDict = {}
    for val in contents[3].split(' '):
        if '\n' in val:
            newVal = val[:len(val)-1]
            defaultDict[labelToIndex[newVal]] = homeIndex
        else:
            defaultDict[labelToIndex[val]] = homeIndex
    return listOfPoints, globalLookup, defaultDict, homeIndex

def run_solver(listOfPoints, globalLookup, defaultDict, homeIndex):
    # create default (empty pathpoints)
    homes = []
    for i in defaultDict.keys():
        homes.append(i)
    start = pathPoint(listOfPoints[homeIndex], set(homes))
    end = pathPoint(listOfPoints[homeIndex], set([]))
    path = [start, end]
    print("===BEFORE===")
    print(path)
    path = simulatedAnnealing(path, listOfPoints, defaultDict, globalLookup)
    print("===AFTER===")
    for i in path:
        print(i.label)
    print(globalLookup)
    return 0

# Given list of path points, generate output file with name
def generate_output(listOfPathPoints, name):
    return 0

def sweep_inputs(range=False):
    # try every input, 
    # read_input ---> list of points, global distance lookup
    # start with some guess ****** pathpoint
    # run_solver on list of pathpoints ---> the correct list of pathpoints
    # generate_output correct list of pathpoint ---> .out

    # TEMP run file
    l, g, d, h = read_input('50.in')
    run_solver(l, g, d, h)

    return 0
sweep_inputs()