from random import randint
# n is number of locations
# k is number of TAs
# ratio is percentage of edges 
# returns dictionary header --> data -->
def generate(n, k, ratio):
    returnData = {}
    returnData['header'] = [n, k]
    data = []
    for _ in range(n):
        dataRow = []
        for _ in range(n):
            append = randint(0, ratio)
            if append > 8:
                append = 'X'
            else:
                append = '1'
            dataRow.append(append)
        data.append(dataRow)
    returnData['data'] = data
    return returnData
    

# data is list of lists
def displayInput(data):
    length = data['header'][0]
    d = data['data']
    for i in range(length):
        s = ""
        for j in range(length):
            s += d[i][j] + " "
        print(s)

