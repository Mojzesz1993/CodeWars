def get_sum(a,b):
    sum = 0
    if a < b:
        while a <= b:
            sum += a
            a += 1
    elif b < a:
        while b <= a:
            sum += b
            b += 1
    elif a == b:
        sum = a

    return sum


get_sum(1, 3)