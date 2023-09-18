def count_by(x, n):
    arr = []
    for i in range (0, n):
        tmp = x * (i + 1)
        arr.append(tmp)
    return arr


print(count_by(2, 10))
print(count_by(3, 10))
print(count_by(50, 10))
print(count_by(100, 10))