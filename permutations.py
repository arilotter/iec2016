import itertools as it
import graph

LOC = ["LOC_1", "LOC_2", "LOC_3", "LOC_4"]

inroute = it.permutations(LOC, 4)
preroute = it.product(["START"], LOC)
postroute = it.product(LOC, "END")

full_permutations = [["START"] + list(route) + ["END"] for route in inroute]


def get_optimal_route():
    cheapest = []
    fastest = []

def cheapest_route():
    all_routes = []
    for route in full_permutations:
        time = 0 #9am
        cost = 0

        for index in range(len(route)-1):
            best = graph.get_optimal_routes(route[index], route[index+1])["cheapest"][time//60]
            cost += best["cost"]
            time += best["time"] * 20

            #print("From %s to %s (time = %s, cost = %s): " % (route[index], route[index+1], time//60, cost))
        all_routes.append({"cost": cost, "time": time, "path": route})


    #best_route = sorted(all_routes, key=lambda x:x['cost'])[0]
    return cheapest_route()




cheapest_route()






