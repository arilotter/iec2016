"""
    The train schedules are stored in a dictionary, accessible by train[line] where line is a single character representing the line the train is on ('A', 'B', 'C', 'D', 'E')
    Each schedule is a list of probability values. Every entry in the schedule list represents one hour's worth of schedules, starting at 9am.
"""

costs = [2, 3, 4]

train_schedules = {
    'A': [
        [0.2, 0.5, 0.3],
        [0.3, 0.4, 0.3],
        [0.4, 0.4, 0.2],
        [0.5, 0.4, 0.1],
        [0.6, 0.3, 0.1],
        [0.6, 0.3, 0.1],
        [0.3, 0.3, 0.4],
        [0.2, 0.3, 0.5],
    ],
    'B': [
        [0.2, 0.5, 0.3],
        [0.3, 0.4, 0.3],
        [0.5, 0.3, 0.2],
        [0.5, 0.4, 0.1],
        [0.5, 0.3, 0.2],
        [0.5, 0.3, 0.2],
        [0.3, 0.3, 0.4],
        [0.2, 0.3, 0.5],
    ],
    'C': [
        [0.5, 0.5, 0.0],
        [0.7, 0.2, 0.1],
        [0.6, 0.2, 0.2],
        [0.8, 0.1, 0.1],
        [0.8, 0.2, 0.0],
        [0.8, 0.2, 0.0],
        [0.4, 0.4, 0.2],
        [0.4, 0.3, 0.3],
    ],
    'D': [
        [0.5, 0.5, 0.0],
        [0.7, 0.2, 0.1],
        [0.8, 0.2, 0.0],
        [0.8, 0.1, 0.1],
        [0.8, 0.2, 0.0],
        [0.8, 0.2, 0.0],
        [0.4, 0.4, 0.2],
        [0.1, 0.1, 0.8],
    ],
    'E': [
        [0.7, 0.3, 0.0],
        [0.7, 0.2, 0.1],
        [0.8, 0.2, 0.0],
        [0.8, 0.1, 0.1],
        [0.7, 0.2, 0.1],
        [0.8, 0.2, 0.0],
        [0.4, 0.4, 0.2],
        [0.2, 0.0, 0.8],
    ],
}

def to_time(minutes):
    hour = minutes // 60
    minutes = minutes % 60
    return "%s:%s" % (hour, str(minutes).zfill(2))