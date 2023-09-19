import math

def find_next_square(sq):
    if math.sqrt(sq).is_integer():
        return (math.sqrt(sq) + 1) ** 2

    else:
        return -1


find_next_square(17)