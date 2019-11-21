from random import randint
# n is number of locations
# k is number of TAs
# ratio is percentage of edges 
# returns dictionary header --> data -->
def generate(n, k, ratio):
    returnData = {}
    returnData['header'] = [n, k, ratio]
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
