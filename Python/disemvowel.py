def disemvowel(string_):
    for i in 'aeiouAEIOU':
        string_ = string_.replace(i, "")
    return string_


disemvowel("What are you, a communist?")