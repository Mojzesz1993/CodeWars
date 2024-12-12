def is_valid_walk(walk):
    if len(walk) != 10:
        print ("False")
        return False
    else:
        N = walk.count('n')
        S = walk.count('s')
        W = walk.count('w')
        E = walk.count('e')
        if N == S and W == E:
            print ("True")
            return True
        else:
            print ("False")
            return False

is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])