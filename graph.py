from schedules import costs, train_schedules
from functools import partial
from operator import itemgetter

def probability_cost(line, time):
    """
    Gets weighted average for the cost of the train
    """
    cost = [2.00, 3.00, 4.00]
    return train_schedules[line][time][0] * cost[0] + train_schedules[line][time][1] * cost[1] + train_schedules[line][time][2] * cost[2]

train = {
    line: partial(probability_cost, line) for line in train_schedules
}

# No cost to walk this edge of the graph
walk = lambda x: 0

#Maps out the graph to use later
graph = {
    'START': {
        'JUNC_1': walk,
    },
    'JUNC_1': {
        'JUNC_2': train['B'],
        'JUNC_4': train['A'],
    },
    'JUNC_2': {
        'END': walk,
        'JUNC_3': train['E'],
        'JUNC_5': train['B'],
    },
    'JUNC_3': {
        'LOC_1': walk,
        'JUNC_4': train['B'],
        'JUNC_5': train['D'],
    },
    'JUNC_4': {
        'JUNC_5': train['C'],
        'JUNC_6': train['B'],
        'JUNC_7': train['A'],
    },
    'JUNC_5': {
        'LOC_2': walk,
        'JUNC_3': train['B'],
    },
    'JUNC_6': {
        'LOC_3': walk,
        'JUNC_1': train['B'],
    },
    'JUNC_7': {
        'LOC_4': walk,
        'JUNC_3': train['A'],
    },
    'LOC_1': {
        'JUNC_3': walk
    },
    'LOC_2': {
        'JUNC_5': walk
    },
    'LOC_3': {
        'JUNC_6': walk
    },
    'LOC_4': {
        'JUNC_7': walk
    },

}

def find_all_routes(graph, start, end, route=[]):
    """
        A recursive approach to dijkstra's algorithm. Finds all the routes between two given nodes
    """
    route = route + [start]
    if start == end:
        return [route]
    if not start in graph:
        return []
    routes = []
    for node in graph[start]:
        if node not in route:
            newroutes = find_all_routes(graph, node, end, route)
            for newroute in newroutes:
                routes.append(newroute)
    return routes


def get_optimal_routes(start, end):
    """
       Searches through all possible paths
       Finds most optimal paths
    """
    all_routes = find_all_routes(graph, start, end)
    cheapest_route = []

    #Optimize for time
    fastest = sorted(all_routes, key=get_time)[0]

    #Optimize for cheap
    for time in range(0, 8):
        time_routes = get_cost(time, all_routes)
        cheapest_route.append(sorted(time_routes, key=lambda x:x['cost'])[0])

    return {"fastest": fastest, "cheapest": cheapest_route}




def get_time(route):
    """
       Gets the time for a specific route
    """
    return sum([0 if node == 'START' or node == 'END' else 1 for node in route[:-1]])


def get_cost(time, route):
    """
       Gets the cost for a specific route
    """
    paths = []
    for full_path in route:
        path_cost = 0
        for index, partial_path in enumerate(full_path[:-1]):
            path_cost += graph[partial_path][full_path[index+1]](time)

        paths.append({"cost": path_cost, "time": get_time(full_path), "path": full_path})
    return paths
