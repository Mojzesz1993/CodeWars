def positive_sum(arr):
    tmp = 0
    for i in arr:
        if i > 0:
            tmp += i
        else:
            continue

    return tmp 





positive_sum([-1,2,3,4,-5])