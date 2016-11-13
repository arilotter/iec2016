import itertools as it
import graph

LOC = ["LOC_1", "LOC_2", "LOC_3", "LOC_4"]

inroute = it.permutations(LOC, 4)
preroute = it.product(["START"], LOC)
postroute = it.product(LOC, "END")

full_permutations = [["START"] + list(route) + ["END"] for route in inroute]

def get_optimal_route():
    cheapest = []
    fastest = get_fastest_route()

def get_fastest_route():
    perm_routes = []
    for perm in full_permutations:
        route = []
        for index, node in enumerate(perm):
            if index > 0:
                route += graph.get_optimal_routes(perm[index - 1], node)["fastest"][:-1]
        perm_routes.append(route)
    fastest = sorted(perm_routes, key=graph.get_time)[0] + ['END']
    return fastest
# graph.get_optimal_routes("LOC_1", "LOC_2")



get_optimal_route()




