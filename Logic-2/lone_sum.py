# Given 3 int values, a b c, return their sum. 
# However, if one of the values is the same as another of the values, it does not count towards the sum.

def lone_sum(a, b, c):
  
  array = [a, b, c]
  sum = a + b + c
  abc_set = set(array)
  
  sum_set = 0        # CodingBat doesn't seem to support the sum function,
  for i in abc_set:  # so instead I have to resort to manually summing the
    sum_set += i     # set, even though sum(abc_set) is a much cleaner way.
  
  if len(abc_set) == 1:
    return 0
    
  else:
    return (2*sum_set) - sum
