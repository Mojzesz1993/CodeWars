import statistics

def find_average(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return statistics.mean(numbers)

find_average([])