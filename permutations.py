import itertools as it
import graph

LOC = ["LOC_1", "LOC_2", "LOC_3", "LOC_4"]

inroute = it.permutations(LOC, 4)
preroute = it.product(["START"], LOC)
postroute = it.product(LOC, "END")

full_permutations = [["START"] + list(route) + ["END"] for route in inroute]

print(full_permutations)
def get_optimal_route():
    cheapest = []
    fastest = []

# graph.get_optimal_routes("LOC_1", "LOC_2")








