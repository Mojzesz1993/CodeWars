def solution(string):
    word = ''
    for i in range(0, len(string)):
        word += string[-i - 1]

    print (word)
    return word


solution('world')
