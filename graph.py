from schedules import costs, train_schedules
from functools import partial

def probability_cost(line, time):
	[sum([costs[index] * probability for index, probability in enumerate(probabilities)]) for hour in train_schedules[line]]
	

train = {
	line: partial(probability_cost, line) for line in train_schedules
}

# No cost to walk this edge of the graph
walk = lambda: 0

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
	}
}

def get_optimal_routes(start, end):
	get_all_routes(start, end)
	shortest_route = None
	cheapest_route = None
	return {
		'shortest': shortest_route,
		'cheapest': cheapest_route
	}

def get_time(route):
	return 

def get_cost(route):
	pass