def solution(s):
    # join the result of recurStrEval
    return ' '.join(recurStrEval(s, '', []))
     
def recurStrEval(str, temp_str, str_arr):
    # if str is blank, append whats left and return
    if not str:
        str_arr.append(temp_str)
        return str_arr
    # if first letter of str is upper, append the temp str to array and then restart cycle
    if str[0].isupper():
        str_arr.append(temp_str)
        temp_str = str[0]
        return recurStrEval(str[1:], temp_str, str_arr)
    # if str is lower, concatenate to the existing string
    if str[0].islower():
        temp_str += str[0]
        return recurStrEval(str[1:], temp_str, str_arr)

solution("helloWorld")
solution("camelCase")
solution("breakCamelCase")