def correct(s):
    correctword = ''
    for i in range (0, len(s)):
        if s[i] == "5":
            correctword += "S"
        elif s[i] == "0":
            correctword += "O"
        elif s[i] == "1":
            correctword += "I"
        else:
            correctword += s[i]
    return correctword


correct("51NGAP0RE")