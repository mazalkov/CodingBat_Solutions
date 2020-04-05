# Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
  if len(str) < 2:
    return str
  
  else:
    midString = str[1:-1]
    return str[-1:] + midString + str[:1]
