def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0:
        if flower2 % 2 == 1:
            return True
        else:
            return False
    else:
        if flower2 % 2 == 0:
            return True
        else:
            return False




lovefunc(5, 6)