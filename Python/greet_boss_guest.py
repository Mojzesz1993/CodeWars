def greet(name, owner):
    if name == owner:
        print("Hello boss")
        return 'Hello boss'
    else:
        print("Hello guest")
        return 'Hello guest'








greet('Daniel', 'Daniel')
greet('Greg', 'Daniel')