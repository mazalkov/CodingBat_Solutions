# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1),
# while the other is "far", differing from both other values by 2 or more. 
# Note: abs(num) computes the absolute value of a number.

def close_far(a, b, c):
  
  close = 0
  far = 0
  
  if abs(b - a) < abs(c - a):
    close, far = b, c
    
  else:
    close, far = c, b
    
  
  return (abs(close - a) <= 1)  and (abs(far - close) >= 2) and (abs(far - a) >= 2)
