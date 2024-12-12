def invert(lst):
    return [n * -1 for n in lst] if len(lst) > 0 else []

invert([1,-2,3,-4,5])