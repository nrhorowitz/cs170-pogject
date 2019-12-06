from simAnn import Point
from simAnn import pathPoint
from simAnn import simulatedAnnealing
from floyd import compute_paths
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
    labelLookup[len(labelLookup) - 1] = labelLookup[len(labelLookup) - 1][:len(labelLookup[len(labelLookup) - 1]) - 1]
    listOfPoints = []
    globalLookup = []
    avgEdge = 0
    numOfEdges = 0
    for i in range(5, 5 + int(contents[0])):
        adjacentList = []
        d = contents[i].split(" ")
        globalLookupRow = []
        for j in range(0, int(contents[0])):
            if 'x' not in d[j]:
                if '\n' in d[j]:
                    globalLookupRow.append(float(d[j][:len(d[j])-1]))
                    avgEdge += float(d[j][:len(d[j])-1])
                    numOfEdges += 1
                else:
                    globalLookupRow.append(float(d[j]))
                    avgEdge += float(d[j])
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
    start = contents[4][:len(contents[4])-1]
    homeIndex = labelToIndex[start]
    defaultDict = {}
    for val in contents[3].split(' '):
        if '\n' in val:
            newVal = val[:len(val)-1]
            defaultDict[labelToIndex[newVal]] = 0 # homeIndex
        else:
            defaultDict[labelToIndex[val]] = 0 # homeIndex
    avgEdge = avgEdge / numOfEdges
    # print(avgEdge)
    return listOfPoints, globalLookup, defaultDict, homeIndex, labelLookup, avgEdge

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
        path = compute_paths(globalLookup, defaultDict, homeIndex)
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
    # for i in range(1, 367):
    # for i in range(3, 10):
    #     print("==============" + str(i))
    l, g, d, h, labelLookup, avgEdge = read_input(0, r)
    path = run_solver(l, g, d, h, avgEdge, True)
        #path = run_solver(l, g, d, h, avgEdge, False)
        # generate_output(path, i, 50, labelLookup)
    return 0
    
sweep_inputs(50)