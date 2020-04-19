# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
# So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
  
  smallerLen = min(len(a), len(b))
  
  counter = 0
  
  for i in range(smallerLen - 1):
    aSub = a[i:i+2]
    bSub = b[i:i+2]
    
    if aSub == bSub:
      counter += 1
      
  return counter
