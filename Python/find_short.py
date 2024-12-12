def find_short(s):
    s = s.split()
    lenght = 10000000
    for i in range (0, len(s)):
        if len(s[i]) < lenght:
            lenght = len(s[i])

    return lenght






find_short("bitcoin take over the world maybe who knows perhaps")
find_short("turns out random test cases are easier than writing out basic ones")
find_short("lets talk about javascript the best language")
find_short("i want to travel the world writing code one day")
find_short("Lets all go on holiday somewhere very cold")  
find_short("Let's travel abroad shall we")