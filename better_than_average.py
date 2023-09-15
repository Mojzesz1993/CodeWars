class_points = [100, 90 , 80, 70, 60, 50, 40, 30, 20, 10, 0]
your_points = 74

def better_than_average(class_points, your_points):
    
    tmp = 0

    for i in range (0, len(class_points)):
        tmp += class_points[i]
    
    average = tmp / len(class_points)

    if your_points > average:
        return True
    else:
        return False 

better_than_average(class_points, your_points)