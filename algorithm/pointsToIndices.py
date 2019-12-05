# Input: List of pathPoints, List of locations
# Output: List of indices of car_cycle and list of indices of droppoff points

def pointToIndices(path_points):
    car_cycle = []
    droppoff_points = {} # maps dropoff location index to a list of index of TA homes
    for point in path_points:
        car_cycle.append(point.label)
        homes_list = []
        for index in point.dropOffs:
            home_list.append(index)
        dropoff_points[point.label] = home_list
    return car_cycle, dropoff_points

# dropOff points example
# {1: [2]}
# locations = ['hi', 'bye', 'nathan']
# homes = ['nathan']
