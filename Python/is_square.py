import math

def is_square(n):
    if n < 0:
        return False
    
    if math.sqrt(n).is_integer():
        return True
    else:
        return False