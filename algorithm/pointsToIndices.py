from student_utils import *
# Input: List of pathPoints, List of locations
# Output: List of indices of car_cycle and list of indices of dropoff points

def costOfPoints(path_points, adjacency_matrix):
    car_cycle = []
    dropoff_mapping = {} # maps dropoff location index to a list of index of TA homes
    for point in path_points:
        car_cycle.append(point.label)
        homes_list = []
        for index in point.dropOffs:
            home_list.append(index)
        dropoff_mapping[point.label] = home_list

    G = adjacency_matrix_to_graph(adjacency_matrix)
    return cost_of_solution(G, car_cycle, dropoff_mapping)

# dropOff points example
# {1: [2]}
# locations = ['hi', 'bye', 'nathan']
# homes = ['nathan']
