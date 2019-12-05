MAX_VALUE = float('inf')

# Given file name, return input in data form
def read_input(file_name):
    f = open("inputs/" + file_name, "r")
    contents = f.readlines()
    data = []
    for i in range(5, 5 + int(contents[0])):
        data.append(contents[i])
    # print(data)
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
    return 0