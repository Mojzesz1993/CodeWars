def sum_array(arr):

    if arr == [] or arr == None or len(arr) == 1:
        return 0

    minimum = min(arr)
    maximum = max(arr)
    tmp = 0
    for i in range (0, len(arr)):
        tmp += arr[i]

    tmp = tmp - minimum - maximum

    return tmp




sum_array ([3, 4, 5, 6, 7, 8, 9])