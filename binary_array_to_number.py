def binary_array_to_number(arr):
    power = len (arr) - 1
    x = 0

    for i in range (0, len (arr)):
        x += arr[i] * 2 ** power
        power -= 1

    print (int(x))
    return int (x)    


binary_array_to_number([0,1,1,1])