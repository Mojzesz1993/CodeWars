def are_you_playing_banjo(name):
    if name[:1] == "R" or name[:1] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


are_you_playing_banjo("rikke")
are_you_playing_banjo("Ricky")
are_you_playing_banjo("Adam")
are_you_playing_banjo("klara")