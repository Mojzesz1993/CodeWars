def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    positive = 0
    negative = 0
    for i in range (0, len(arr)):
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += arr[i]
    if positive or negative != 0:
        return [positive, negative]
    elif positive == 0 and negative == 0:
        return [0, 0]
    