def likes (names):
    if len (names) == 0:
        return "no one likes this"
    elif len (names) == 1:
        print(names[0] + " likes this")
        return names[0] + " likes this"
    elif len (names) == 2:
        return names[0] + " and " + names[1] + " like this"
    elif len (names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    elif len (names) > 3:
        x = len (names) - 2
        return names[0] + ", " + names[1] + " and " + str(x) + " others like this"
    

likes(["Alex"])