def digitize(n):
    x = []
    for i in range (0, len(str(n))):
        x.insert(0, int(str(n)[i:i+1]))
        print(x)

    return x


digitize(984764738)