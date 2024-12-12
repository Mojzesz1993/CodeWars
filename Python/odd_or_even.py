def odd_or_even(arr):
    tmp = 0
    for i in arr:
        tmp += i

    if tmp %2 == 0:
        print ("even")
        return "even"
    else:
        print ("odd")
        return "odd"