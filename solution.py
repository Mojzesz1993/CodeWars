def solution(string, ending):
  lenCompare = len(string) - len(ending)
  string3 = string[lenCompare:]
  if string3 == ending:
    return True
  else:
    return False

solution( "fails",   "ails"  )
solution( "samurai", "ai"    )