import schedules

print(schedules.trainA)

def trainA(time):
	return 3

def trainB(time):
	return 2

def trainC(time):
	return 0

def walk(time):
	return 0

graph = {
	'START': [['JUNCTION_1', walk],
	'JUNCTION_1': {
		'JUNCTION_2': trainB,
		'JUNCTION_4': trainA
	},
	'JUNCTION_2': {
		'END': walk,
		'JUNCTION_5': trainB,
		'JUNCTION_3': trainE
	},
	'JUNCTION_3': {
		'JUNCTION_5': {

		}
	}
}
