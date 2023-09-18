def longest(s1, s2):
    return "".join(sorted([c for c in set(s1 + s2)]))


longest("aretheyhere", "yestheyarehere")
longest("loopingisfunbutdangerous", "lessdangerousthancoding")
longest("inmanylanguages", "theresapairoffunctions")