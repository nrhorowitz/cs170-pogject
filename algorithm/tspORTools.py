"""Simple travelling salesman problem between cities."""
# python3 -m pip install --upgrade --user ortools

from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp



def create_data_model(dataInput, homeIndex):
    """Stores the data for the problem."""
    data = {}
    if dataInput:
        data['distance_matrix'] = dataInput
    else:
        data['distance_matrix'] = [[0, 5, 8, 250, 250, 6, 6, 7, 8, 5, 5, 6, 8, 6, 250, 6, 8, 7, 6, 7, 8, 5, 6, 8, 9], [5, 0, 9, 5, 6, 250, 8, 250, 8, 9, 250, 250, 8, 5, 6, 7, 250, 7, 9, 6, 6, 250, 8, 7, 250], [8, 9, 0, 6, 9, 5, 5, 5, 9, 6, 7, 250, 250, 7, 6, 5, 6, 9, 6, 7, 7, 8, 250, 8, 7], [250, 5, 6, 0, 9, 6, 6, 250, 250, 9, 9, 9, 250, 250, 7, 7, 9, 7, 8, 250, 9, 9, 9, 6, 5], [250, 6, 9, 9, 0, 250, 250, 7, 7, 5, 6, 8, 7, 250, 8, 5, 250, 8, 8, 6, 7, 9, 250, 8, 250], [6, 250, 5, 6, 250, 0, 8, 250, 8, 8, 250, 6, 250, 250, 6, 5, 250, 7, 9, 5, 7, 7, 7, 8, 7], [6, 8, 5, 6, 250, 8, 0, 6, 9, 6, 8, 8, 250, 5, 250, 9, 250, 9, 250, 9, 6, 7, 9, 7, 8], [7, 250, 5, 250, 7, 250, 6, 0, 7, 9, 8, 9, 5, 250, 9, 8, 9, 7, 7, 8, 6, 9, 250, 5, 6], [8, 8, 9, 250, 7, 8, 9, 7, 0, 8, 250, 7, 5, 9, 8, 250, 9, 8, 5, 7, 5, 5, 9, 250, 6], [5, 9, 6, 9, 5, 8, 6, 9, 8, 0, 250, 8, 250, 6, 9, 6, 5, 250, 8, 250, 5, 9, 6, 9, 250], [5, 250, 7, 9, 6, 250, 8, 8, 250, 250, 0, 5, 5, 250, 5, 9, 7, 9, 5, 8, 250, 5, 250, 8, 8], [6, 250, 250, 9, 8, 6, 8, 9, 7, 8, 5, 0, 6, 7, 250, 7, 7, 5, 7, 5, 250, 9, 5, 5, 8], [8, 8, 250, 250, 7, 250, 250, 5, 5, 250, 5, 6, 0, 9, 5, 8, 5, 9, 7, 9, 8, 9, 250, 250, 250], [6, 5, 7, 250, 250, 250, 5, 250, 9, 6, 250, 7, 9, 0, 9, 250, 250, 6, 5, 6, 9, 9, 7, 6, 7], [250, 6, 6, 7, 8, 6, 250, 9, 8, 9, 5, 250, 5, 9, 0, 6, 250, 9, 8, 8, 7, 8, 250, 250, 9], [6, 7, 5, 7, 5, 5, 9, 8, 250, 6, 9, 7, 8, 250, 6, 0, 9, 6, 5, 7, 250, 5, 9, 7, 8], [8, 250, 6, 9, 250, 250, 250, 9, 9, 5, 7, 7, 5, 250, 250, 9, 0, 5, 5, 5, 9, 6, 9, 9, 5], [7, 7, 9, 7, 8, 7, 9, 7, 8, 250, 9, 5, 9, 6, 9, 6, 5, 0, 5, 6, 7, 9, 6, 6, 250], [6, 9, 6, 8, 8, 9, 250, 7, 5, 8, 5, 7, 7, 5, 8, 5, 5, 5, 0, 8, 250, 9, 9, 8, 5], [7, 6, 7, 250, 6, 5, 9, 8, 7, 250, 8, 5, 9, 6, 8, 7, 5, 6, 8, 0, 250, 9, 8, 9, 6], [8, 6, 7, 9, 7, 7, 6, 6, 5, 5, 250, 250, 8, 9, 7, 250, 9, 7, 250, 250, 0, 9, 250, 6, 250], [5, 250, 8, 9, 9, 7, 7, 9, 5, 9, 5, 9, 9, 9, 8, 5, 6, 9, 9, 9, 9, 0, 9, 7, 8], [6, 8, 250, 9, 250, 7, 9, 250, 9, 6, 250, 5, 250, 7, 250, 9, 9, 6, 9, 8, 250, 9, 0, 6, 250], [8, 7, 8, 6, 8, 8, 7, 5, 250, 9, 8, 5, 250, 6, 250, 7, 9, 6, 8, 9, 6, 7, 6, 0, 8], [9, 250, 7, 5, 250, 7, 8, 6, 6, 250, 8, 8, 250, 7, 9, 8, 5, 250, 5, 6, 250, 8, 250, 8, 0]]

    data['num_vehicles'] = 1
    data['depot'] = homeIndex
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


def main(data):
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model(data)

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

def generateStartingPointPaths(globalLookup, homeIndex):
    # convert all x to relative inf
    MAX_VALUE = 10000000
    # deepcopy
    data = []
    for i in range(len(globalLookup)):
        dataRow = []
        for j in range(len(globalLookup)):
            v = globalLookup[i][j]
            if v == 'x':
                dataRow.append(MAX_VALUE)
            else:
                dataRow.append(v)
        data.append(dataRow)
    for i in range(len(data)):
        data[i][i] = 0

    main(data, homeIndex)
    print(data)

    