from student_utils import *
# Input: List of pathPoints, List of locations
# Output: List of indices of car_cycle and list of indices of dropoff points

def costOfPoints(path_points, adjacency_matrix, final = False):
    car_cycle = []
    dropoff_mapping = {} # maps dropoff location index to a list of index of TA homes
    for point in path_points:
        car_cycle.append(point.label)
        homes_list = []
        for index in point.dropoffs:
            homes_list.append(index)
        if homes_list:
            if point.label in dropoff_mapping:
                dropoff_mapping[point.label] += homes_list
            else:
                dropoff_mapping[point.label] = homes_list
    
    G = adjacency_matrix_to_graph(adjacency_matrix)[0]
    # print(car_cycle, dropoff_mapping)
    return cost_of_solution(G, car_cycle, dropoff_mapping)

# dropOff points example
# {1: [2]}
# locations = ['hi', 'bye', 'nathan']
# homes = ['nathan']
