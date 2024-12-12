def smash(words):
    if words == []:
        return ""
    
    if len(words) == 1:
        return words[0]
     
    return " ".join(words)