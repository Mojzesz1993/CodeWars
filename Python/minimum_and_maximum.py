def minimum(arr):
    tmp = arr [0]
    for i in range (0, len(arr)):
        if arr [i] < tmp:
            tmp = arr [i]
        else:
            continue
    return tmp

def maximum(arr):
    tmp = arr [0]
    for i in range (0, len(arr)):
        if arr [i] > tmp:
            tmp = arr [i]
        else:
            continue
    return tmp
    
    
    
minimum([-52, 56, 30, 29, -54, 0, -110])
minimum([-1, -2, -3, -4, -5, -10])

maximum([534,43,2,1,3,4,5,5,443,443,555,555])
maximum([4,6,2,1,9,63,-134,566])