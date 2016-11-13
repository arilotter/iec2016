#!/usr/bin/env python3

from schedules import to_time
import permutations
import graph

print("Calculating optimal routes")
optimal = permutations.get_optimal_route()

#Fastest

print("Fastest solution:")
print("\tTotal time: %s" % (graph.get_time(optimal["fastest"])*20))

thetime = 0
for path in optimal["fastest"]:

    output_string = path.replace("JUNC_", "Junction ")
    output_string = output_string.replace("LOC_", "Location ")
    print("\t%s\t%s" % (thetime, output_string))


    thetime += 0 if path == 'START' or path == 'END' else 20


thetime = 0

print("Cheapest solution: ")
for path in optimal["cheapest"]["path"]:

    output_string = path.replace("JUNC_", "Junction ")
    output_string = output_string.replace("LOC_", "Location ")
    print("\t%s\t%s" % (thetime, output_string))


    thetime += 0 if path == 'START' or path == 'END' else 20
