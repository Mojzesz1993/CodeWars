def number(bus_stops):
    comein = 0
    comeout = 0
    for i in range (0, len(bus_stops)):
        tmp = bus_stops[i]
        comein += tmp[0]
        comeout += tmp[1]

    return comein - comeout








number([[10,0],[3,5],[5,8]])
number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])
number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]])