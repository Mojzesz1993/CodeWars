def grow(arr):
    multiple = 1
    for i in range (0, len(arr)):
        multiple *= arr[i]
    return multiple






grow([1, 2, 3])