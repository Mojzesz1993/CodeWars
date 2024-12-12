def validate_pin(pin):
    l = len(str(pin))

    ill = ['.', '-', '+', '/', ':', '\\', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Q', 'H']

    for x in range(len(ill)):
        if ill[x] in str(pin):
            return False

    if len(str(pin)) == 4:
        return True
    elif len(str(pin)) == 6:
        return True
    else:
        return False
    
validate_pin(1234)