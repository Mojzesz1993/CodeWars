def dig_pow(n, p):
    value = 0
    for digit in str(n):
        value += int(digit)**p
        p += 1
    for k in range(1,value):
        if value/k == n:
            return k
    return -1

dig_pow(71, 5)