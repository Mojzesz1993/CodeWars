def count_sheep(n):
    sheep = ''
    for i in range (1, n + 1):
        sheep += str(i) + ' sheep...'

    print (sheep)
    return sheep




count_sheep(5)