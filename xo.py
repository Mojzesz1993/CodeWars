def xo(s):
    s = s.lower()
    X = s.count('x')
    O = s.count('o')
    if X == O:
        return True
    else:
        return False