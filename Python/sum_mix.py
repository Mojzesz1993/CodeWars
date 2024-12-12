def sum_mix(arr):
    tmp = 0
    iteration = 0
    for i in arr:
        tmp += int(arr[iteration])
        iteration += 1

    print(tmp)
    return int(tmp)




sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0'])