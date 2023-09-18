def double_char(s):
    tmp = ''
    for i in range (0, len(s)):
        tmp += s[i] + s[i]

    print(tmp)
    return str(tmp)


double_char("Hello!")