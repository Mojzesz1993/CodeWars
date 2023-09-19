def fake_bin(x):
    bin = ''
    y = 0
    for i in range (len(x)):
        y = x[i]
        if int(y) < 5:
            bin += "0"
        else:
            bin += "1"
    print(bin)
    return bin


fake_bin("123865123763")