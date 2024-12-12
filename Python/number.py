def number(lines):

    finaly_lines = []
    iteration = 1

    for i in lines:
         
        tmp = ''
        tmp = str(iteration) + ': ' + lines[iteration - 1]
        finaly_lines.append(tmp)
        iteration += 1

    print(finaly_lines)
    return finaly_lines



number(["a", "b", "c"])