def get_grade(s1, s2, s3):
    s = (s1 + s2 + s3) / 3
    if s < 60: return "F"
    elif s < 70: return "D"
    elif s < 80: return "C"
    elif s < 90: return "B"
    elif s <= 100: return "A"