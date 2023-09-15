def to_jaden_case(string):
    stringarr = string.split()
    
    for i in range (0, len(stringarr)):
        tmp = stringarr[i]
        stringarr[i] = tmp.capitalize()

    return (" ".join(stringarr))



to_jaden_case("How can mirrors be real if our eyes aren't real")