import itertools as it
import graph

LOC = ["LOC_1", "LOC_2", "LOC_3", "LOC_4"]

inroute = it.permutations(LOC, 4)
preroute = it.product(["START"], LOC)
postroute = it.product(LOC, "END")

full_permutations = [["START"] + list(route) + ["END"] for route in inroute]

def get_optimal_route():
    return {
        "cheapest": cheapest_route(),
        "fastest": get_fastest_route()
    }

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



def cheapest_route():
    all_routes = []
    for route in full_permutations:
        time = 0 #9am
        cost = 0

        for index in range(len(route)-1):
            best = graph.get_optimal_routes(route[index], route[index+1])["cheapest"][time//3]
            cost += best["cost"]
            time += best["time"]

            #print("From %s to %s (time = %s, cost = %s): " % (route[index], route[index+1], time//60, cost))
        all_routes.append({"cost": cost, "time": time, "path": route})


    best_route = sorted(all_routes, key=lambda x:x['cost'])[0]
    return best_route