from simAnn import Point
from simAnn import pathPoint
from simAnn import simulatedAnnealing
from floyd import compute_paths
import numpy as np 
# from tspORTools import generateStartingPointPaths

MAX_VALUE = float('inf')

# Given file name, return input in data form
# convert input to null path and list of points and distance lookup
# returns list of points, global lookup for distance between points
def read_input(index, size):
    file_name = str(index) + "_" + str(size) + ".in"
    f = open("../inputs/" + file_name, "r")
    contents = f.readlines()
    labelLookup = contents[2].split(" ")
    if len(labelLookup[len(labelLookup) - 1]) == 0:
        labelLookup.pop()
    labelLookup[len(labelLookup) - 1] = labelLookup[len(labelLookup) - 1][:len(labelLookup[len(labelLookup) - 1]) - 1]
    listOfPoints = []
    globalLookup = []
    avgEdge = []
    numOfEdges = 0
    for i in range(5, 5 + int(contents[0])):
        adjacentList = []
        d = contents[i].split(" ")
        globalLookupRow = []
        for j in range(0, int(contents[0])):
            if 'x' not in d[j]:
                if '\n' in d[j]:
                    if d[j] != '\n':
                        globalLookupRow.append(float(d[j][:len(d[j])-1]))
                        avgEdge.append(float(d[j][:len(d[j])-1]))
                        numOfEdges += 1
                else:
                    globalLookupRow.append(float(d[j]))
                    avgEdge.append(float(d[j]))
                    numOfEdges += 1
                adjacentList.append(j)
            else:
                globalLookupRow.append('x')
        globalLookup.append(globalLookupRow)
        p = Point(i - 5, adjacentList, labelLookup[i - 5])
        listOfPoints.append(p)
    labelToIndex = {}
    for i in range(len(labelLookup)):
        labelToIndex[labelLookup[i]] = i
    start = 0
    if len(contents[4].split(" ")) > 1:
        start = contents[4].split(" ")[0]
    else:
        start = contents[4][:len(contents[4])-1]
    homeIndex = labelToIndex[start]
    defaultDict = {}
    for val in contents[3].split(' '):
        if len(val) == 0:
            a = 1
        elif '\n' in val:
            if val != '\n':
                newVal = val[:len(val)-1]
                defaultDict[labelToIndex[newVal]] = 0 # homeIndex
        else:
            defaultDict[labelToIndex[val]] = 0 # homeIndex
    quantileData = []
    quantileData.append(np.quantile(avgEdge, .25))
    quantileData.append(np.quantile(avgEdge, .5))
    quantileData.append(np.quantile(avgEdge, .75))
    return listOfPoints, globalLookup, defaultDict, homeIndex, labelLookup, quantileData

def run_solver(listOfPoints, globalLookup, defaultDict, homeIndex, avgEdge, starting):
    # create default (empty pathpoints)
    path = []
    if (starting):
        homes = []
        for i in defaultDict.keys():
            homes.append(i)
        start = pathPoint(listOfPoints[homeIndex], set(homes))
        end = pathPoint(listOfPoints[homeIndex], set([]))
        path = [start, end]
    else:
        path = compute_paths(globalLookup, listOfPoints, homeIndex)
    path = simulatedAnnealing(path, listOfPoints, defaultDict, globalLookup, avgEdge)
    return path

# Given list of path points, generate output file with name
def generate_output(listOfPathPoints, index, size, labelLookup):
    file_name = str(index) + "_" + str(size) + ".out"
    f = open("../outputs/" + file_name, "w+")
    dropoffCount = 0
    dropoffIndices = []   
    s1 = ''
    for i in range(len(listOfPathPoints) - 1):
        s1 += listOfPathPoints[i].rawLabel + " "
        if len(listOfPathPoints[i].dropoffs) > 0:
            dropoffCount += 1
            dropoffIndices.append(i)
    s1 += listOfPathPoints[len(listOfPathPoints) - 1].rawLabel
    if len(listOfPathPoints[len(listOfPathPoints) - 1].dropoffs) > 0:
            dropoffCount += 1
            dropoffIndices.append(len(listOfPathPoints) - 1)
    f.write(s1 + "\n")
    f.write(str(dropoffCount) + "\n")
    for i in dropoffIndices:
        s = listOfPathPoints[i].rawLabel + " "
        for j in listOfPathPoints[i].dropoffs:
            s += labelLookup[j] + " "
        s = s[:len(s)-1]
        f.write(s + "\n")
    return 0

def sweep_inputs(r=False):
    # try every input, 
    # read_input ---> list of points, global distance lookup
    # start with some guess ****** pathpoint
    # run_solver on list of pathpoints ---> the correct list of pathpoints
    # generate_output correct list of pathpoint ---> .out
    # for i in range(1, 367)::
    num = 121
    print("=====FILE: " + str(num) + "_" + str(r) + "=====")
    l, g, d, h, labelLookup, avgEdge = read_input(num, r)
    print(avgEdge)
    path = run_solver(l, g, d, h, avgEdge, True)
    for i in range((len(path))):
        if (path[i].dropoffs):
            for j in range(i + 1, len(path)):
                if(path[i].label == path[j].label):
                    if len(path[j].dropoffs) > 0:
                        path[i].dropoffs = path[i].dropoffs | path[j].dropoffs
                        path[j].dropoffs = set()
    for i in path:
        print(i.label, i.dropoffs)
    generate_output(path, num, 50, labelLookup)
    print('\n')

    # for i in range(9, 367):
    #     print("=====FILE: " + str(i) + "_" + str(r) + "=====")
    #     l, g, d, h, labelLookup, avgEdge = read_input(i, r)
    #     print(avgEdge)
    #     path = run_solver(l, g, d, h, avgEdge, True)
    #     generate_output(path, i, 50, labelLookup)
    #     print('\n')
    


    return 0

    
sweep_inputs(50)