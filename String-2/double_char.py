# Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
  
  string = ""
  
  for i in range(0, len(str)):
    string += 2 * str[i]
    
  return string
