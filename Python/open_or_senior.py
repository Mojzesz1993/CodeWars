def open_or_senior(data):
    status = []
    for i in range (0, len(data)):
        if data[i][0] >= 55 and data[i][1] > 7:
            status.append("Senior")
        else:
            status.append("Open")

    return status







open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])