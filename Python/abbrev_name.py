def abbrev_name(name):
    arr = name.split()
    name = (arr[0][0].upper() + "." + arr[1][0].upper())
    return str(name)






abbrev_name("Sam Harris")
abbrev_name("patrick feenan")