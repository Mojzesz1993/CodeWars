def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True


            


is_isogram("isIsogram")
is_isogram("Dermatoglyphics")