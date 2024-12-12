def is_palindrome(string):
    string = string.lower()
    return str(string) == str(string)[::-1]