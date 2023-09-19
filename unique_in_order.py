def unique_in_order(sequence):
    if sequence == "" or sequence == [] or sequence == ():
        return []
    
    x = sequence[0]
    finish = []
    finish.append(x)

    for i in range (1, len (sequence)):
        if sequence[i] == sequence[i-1]:
            continue
        else:
            finish.append(sequence[i])

    print(finish)
    return finish

unique_in_order("AAAABBBCCDAABBB")