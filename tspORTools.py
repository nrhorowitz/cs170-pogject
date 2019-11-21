"""Simple travelling salesman problem between cities."""
# python3 -m pip install --upgrade --user ortools

from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp



def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = [
        [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
        [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
        [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
        [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
        [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
        [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
        [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
        [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
        [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
        [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
        [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
        [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
        [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0],
    ]  # yapf: disable

    data['distance_matrix'] = [[0, 27, 23, 24, 31, 800, 23, 800, 20, 27, 34, 34, 35, 24, 32, 26, 20, 36, 24, 25], [27, 0, 22, 39, 800, 36, 32, 25, 36, 22, 800, 25, 20, 28, 22, 24, 27, 37, 35, 30], [23, 22, 0, 36, 21, 37, 26, 35, 25, 37, 23, 31, 33, 28, 800, 20, 36, 28, 33, 38], [24, 39, 36, 0, 21, 30, 29, 34, 24, 31, 24, 36, 30, 39, 33, 32, 34, 30, 33, 34], [31, 800, 21, 21, 0, 25, 32, 28, 34, 39, 30, 26, 21, 33, 800, 23, 800, 20, 30, 800], [800, 36, 37, 30, 25, 0, 27, 24, 33, 30, 21, 38, 32, 33, 34, 38, 800, 26, 27, 20], [23, 32, 26, 29, 32, 27, 0, 24, 24, 800, 31, 27, 35, 800, 31, 32, 29, 32, 22, 31], [800, 25, 35, 34, 28, 24, 24, 0, 30, 34, 33, 20, 36, 21, 37, 38, 39, 36, 22, 22], [20, 36, 25, 24, 34, 33, 24, 30, 0, 800, 32, 22, 26, 26, 29, 36, 27, 30, 25, 34], [27, 22, 37, 31, 39, 30, 800, 34, 800, 0, 20, 31, 34, 22, 21, 27, 20, 24, 26, 33], [34, 800, 23, 24, 30, 21, 31, 33, 32, 20, 0, 39, 32, 29, 27, 38, 20, 31, 39, 36], [34, 25, 31, 36, 26, 38, 27, 20, 22, 31, 39, 0, 37, 24, 800, 39, 37, 800, 34, 23], [35, 20, 33, 30, 21, 32, 35, 36, 26, 34, 32, 37, 0, 34, 800, 25, 800, 32, 31, 34], [24, 28, 28, 39, 33, 33, 800, 21, 26, 22, 29, 24, 34, 0, 31, 36, 36, 39, 31, 21], [32, 22, 800, 33, 800, 34, 31, 37, 29, 21, 27, 800, 800, 31, 0, 28, 30, 36, 31, 30], [26, 24, 20, 32, 23, 38, 32, 38, 36, 27, 38, 39, 25, 36, 28, 0, 29, 29, 800, 31], [20, 27, 36, 34, 800, 800, 29, 39, 27, 20, 20, 37, 800, 36, 30, 29, 0, 23, 24, 36], [36, 37, 28, 30, 20, 26, 32, 36, 30, 24, 31, 800, 32, 39, 36, 29, 23, 0, 25, 35], [24, 35, 33, 33, 30, 27, 22, 22, 25, 26, 39, 34, 31, 31, 31, 800, 24, 25, 0, 38], [25, 30, 38, 34, 800, 20, 31, 22, 34, 33, 36, 23, 34, 21, 30, 31, 36, 35, 38, 0]]



    data['num_vehicles'] = 1
    data['depot'] = 0
    return data


def print_solution(manager, routing, assignment):
    """Prints assignment on console."""
    print('Objective: {} miles'.format(assignment.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route for vehicle 0:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = assignment.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Route distance: {}miles\n'.format(route_distance)


def main():
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    assignment = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if assignment:
        print_solution(manager, routing, assignment)


if __name__ == '__main__':
    main()