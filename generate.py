from random import randint
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

labelLookup = {
    0: "A",
}

# n is number of locations
# k is number of TAs
# ratio is percentage of edges
# returns dictionary header --> data -->
def is_metric(G):
    shortest = dict(nx.floyd_warshall(G))
    for u, v, datadict in G.edges(data=True):
        if abs(shortest[u][v] - datadict["weight"]) >= 0.00001:

            return False
    return True

def generate(n, k, ratio):
    returnData = {}
    returnData['header'] = [n, k, ratio, 2*ratio*n * 10]
    data = []
    for i in range(n):
        dataRow = []
        for j in range(n):
            append = randint(ratio, (2*ratio) - 1)
            kVal = randint(0, 100)
            if k > kVal:
                append = 2*ratio*n
            if i == j:
                append = 0
            dataRow.append(append)
        data.append(dataRow)
    # make sure symmmetric
    for i in range(n):
        for j in range(i, n):
            data[i][j] = data[j][i]
    returnData['data'] = data
    return returnData


# data is list of lists
def displayInput(data):
    length = data['header'][0]
    d = data['data']
    for i in range(length):
        s = ""
        for j in range(length):
            s += str(d[i][j]) + " "
        print(s)

def displayRaw(data):
    print(data['data'])

def displayGraph(data, name = "simple_path.png"):
    d = data['data']
    G = nx.Graph()
    noEdge = data['header'][3]
    for i in range(len(d)):
        G.add_node("A" + str(i))
    for i in range(len(d)):
        for j in range(len(d)):
            length = d[i][j]
            if not length == noEdge:
                G.add_edge("A" + str(i), "A" + str(j), weight=length)

    nx.draw(G)
    plt.savefig(name) # save as png
    plt.clf()
    plt.show() # display


def isConnected(data):
    graph1 = {
        'A' : ['B','S'],
        'B' : ['A'],
        'C' : ['D','E','F','S'],
        'D' : ['C'],
        'E' : ['C','H'],
        'F' : ['C','G'],
        'G' : ['F','S'],
        'H' : ['E','G'],
        'S' : ['A','C','G']
    }

    def dfs(graph, node, visited):
        if node not in visited:
            visited.append(node)
            for n in graph[node]:
                dfs(graph,n, visited)
        return visited

    visited = dfs(graph1,'A', [])
    print(visited)

def appendEdge(data, v1, v2, weight):
    d = data['data']
    d[v1][v2] = weight
    d[v2][v1] = weight

def addGraphs(graph1, graph2):
    randEdgeX, randEdgeY = randint(graph1['header'][0], graph1['header'][0] * 2 - 1), randint(0, graph1['header'][0] - 1)
    randLen = randint(graph1['header'][2], graph1['header'][2] * 2 - 1)
    graph1['header'][0] += graph2['header'][0]
    graph1['header'][1] += graph2['header'][1]
    for i in range(len(graph1['data'])):
        graph1['data'].append([graph1['header'][3]] * len(graph1['data'][i]) + graph2['data'][i])
        graph1['data'][i] += [graph1['header'][3]] * len(graph2['data'][i])
    graph1['data'][randEdgeX][randEdgeY], graph1['data'][randEdgeY][randEdgeX] = randLen, randLen
    print(randEdgeX, randEdgeY, randLen)
def makeMetricComplete(graph):
    data = graph['data']
    npy = np.array(data)
    shortest = dict(nx.floyd_warshall(nx.from_numpy_matrix(npy)))
    print(shortest)
    for i in range(len(data)):
        for j in range(i, len(data)):
            if(data[i][j] == graph['header'][3]):
                data[i][j], data[j][i] = shortest[i][j] - .0001, shortest[i][j] - .0001, 
def generateOwen(n):
    graph = generate(50, 100, n)
    # index, index, weight
    # appendEdge(graph, index, index, weight)
    # appendEdge(graph, index, index, weight)
    # appendEdge(graph, index, index, weight)
    # appendEdge(graph, index, index, weight)
    # h - 1, l + 21
    lookup = {
        ""
    }
    appendEdge(graph, 0, 1, randint(n, (2*n) - 1))
    appendEdge(graph, 0, 22, randint(n, (2*n) - 1))
    appendEdge(graph, 1, 22, randint(n, (2*n) - 1))
    appendEdge(graph, 22, 23, randint(n, (2*n) - 1))
    appendEdge(graph, 23, 2, randint(n, (2*n) - 1))
    appendEdge(graph, 2, 3, randint(n, (2*n) - 1))
    appendEdge(graph, 2, 22, randint(n, (2*n) - 1))
    appendEdge(graph, 22, 3, randint(n, (2*n) - 1))
    appendEdge(graph, 3, 24, randint(n, (2*n) - 1))
    appendEdge(graph, 24, 25, randint(n, (2*n) - 1))
    appendEdge(graph, 25, 4, randint(n, (2*n) - 1))
    appendEdge(graph, 4, 26, randint(n, (2*n) - 1))
    appendEdge(graph, 26, 27, randint(n, (2*n) - 1))
    appendEdge(graph, 27, 5, randint(n, (2*n) - 1))
    appendEdge(graph, 5, 28, randint(n, (2*n) - 1))
    appendEdge(graph, 28, 29, randint(n, (2*n) - 1))
    appendEdge(graph, 29, 30, randint(n, (2*n) - 1))
    appendEdge(graph, 24, 30, randint(n, (2*n) - 1))
    appendEdge(graph, 29, 31, randint(n, (2*n) - 1))
    appendEdge(graph, 31, 32, randint(n, (2*n) - 1))
    appendEdge(graph, 32, 6, randint(n, (2*n) - 1))
    appendEdge(graph, 6, 7, randint(n, (2*n) - 1))
    appendEdge(graph, 7, 33, randint(n, (2*n) - 1))
    appendEdge(graph, 33, 38, randint(n, (2*n) - 1))
    appendEdge(graph, 8, 34, randint(n, (2*n) - 1))
    appendEdge(graph, 34, 35, randint(n, (2*n) - 1))
    appendEdge(graph, 31, 35, randint(n, (2*n) - 1))
    appendEdge(graph, 31, 34, randint(n, (2*n) - 1))
    appendEdge(graph, 3, 36, randint(n, (2*n) - 1))
    appendEdge(graph, 3, 10, randint(n, (2*n) - 1))
    appendEdge(graph, 10, 11, randint(n, (2*n) - 1))
    appendEdge(graph, 36, 10, randint(n, (2*n) - 1))
    appendEdge(graph, 9, 10, randint(n, (2*n) - 1))
    appendEdge(graph, 36, 9, randint(n, (2*n) - 1))
    appendEdge(graph, 9, 35, randint(n, (2*n) - 1))
    appendEdge(graph, 35, 30, randint(n, (2*n) - 1))
    appendEdge(graph, 22, 10, randint(n, (2*n) - 1))
    appendEdge(graph, 10, 37, randint(n, (2*n) - 1))
    appendEdge(graph, 22, 37, randint(n, (2*n) - 1))
    appendEdge(graph, 37, 21, randint(n, (2*n) - 1))
    appendEdge(graph, 37, 39, randint(n, (2*n) - 1))
    appendEdge(graph, 39, 19, randint(n, (2*n) - 1))
    appendEdge(graph, 19, 20, randint(n, (2*n) - 1))
    appendEdge(graph, 20, 21, randint(n, (2*n) - 1))
    appendEdge(graph, 20, 38, randint(n, (2*n) - 1))
    appendEdge(graph, 38, 21, randint(n, (2*n) - 1))
    appendEdge(graph, 39, 11, randint(n, (2*n) - 1))
    appendEdge(graph, 35, 42, randint(n, (2*n) - 1))
    appendEdge(graph, 9, 42, randint(n, (2*n) - 1))
    appendEdge(graph, 11, 42, randint(n, (2*n) - 1))
    appendEdge(graph, 11, 40, randint(n, (2*n) - 1))
    appendEdge(graph, 40, 42, randint(n, (2*n) - 1))
    appendEdge(graph, 18, 42, randint(n, (2*n) - 1))
    appendEdge(graph, 18, 17, randint(n, (2*n) - 1))
    appendEdge(graph, 17, 12, randint(n, (2*n) - 1))
    appendEdge(graph, 12, 40, randint(n, (2*n) - 1))
    appendEdge(graph, 40, 43, randint(n, (2*n) - 1))
    appendEdge(graph, 42, 46, randint(n, (2*n) - 1))
    appendEdge(graph, 12, 44, randint(n, (2*n) - 1))
    appendEdge(graph, 38, 21, randint(n, (2*n) - 1))
    appendEdge(graph, 17, 49, randint(n, (2*n) - 1))
    appendEdge(graph, 18, 49, randint(n, (2*n) - 1))
    appendEdge(graph, 21, 16, randint(n, (2*n) - 1))
    appendEdge(graph, 43, 15, randint(n, (2*n) - 1))
    appendEdge(graph, 44, 13, randint(n, (2*n) - 1))
    appendEdge(graph, 14, 13, randint(n, (2*n) - 1))
    appendEdge(graph, 41, 1, randint(n, (2*n) - 1))
    appendEdge(graph, 45, 20, randint(n, (2*n) - 1))
    appendEdge(graph, 47, 45, randint(n, (2*n) - 1))
    appendEdge(graph, 48, 47, randint(n, (2*n) - 1))
    return graph

a = generate(5, 2, 100)
displayGraph(a, "graph1")
print(is_metric(nx.from_numpy_matrix(np.array(a['data']))))
b = generate(5, 2, 100)
displayGraph(b, "graph2")
print(np.array(a['data']))
addGraphs(a, b)
print(is_metric(nx.from_numpy_matrix(np.array(a['data']))))
displayGraph(a)
print(np.array(a['data']))
makeMetricComplete(a)
print(np.array(a['data']))
displayGraph(a, "graph3")

print(is_metric(nx.from_numpy_matrix(np.array(a['data']))))

