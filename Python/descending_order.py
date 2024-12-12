import math

def descending_order(num):
    arr = []
    tmp = num

    for i in range (0, len(str(num))):

        modulo = num % 10
        num = math.floor(num/10)
        arr.append(modulo)
        modulo = math.floor(modulo/10)
        
    final = []
    for i in range (0, len(str(tmp))):
        final.append(arr.pop(arr.index(max(arr))))

    x = 0

    for i in range (0, len(final)):
        x += final[i]
        x *= 10

    x = x / 10
    x = int(x)
    return x
    

descending_order(123455)