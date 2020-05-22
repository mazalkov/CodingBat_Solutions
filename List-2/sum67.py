# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 
# (every 6 will be followed by at least one 7). Return 0 for no numbers.

def sum67(nums):
  
  ignore = False
  sum, i = 0, 0
  
  if len(nums) == 0:
    return 0
  
  while i < len(nums):
    if ignore:
      if nums[i] == 7:
        ignore = False
    
    else:
      if nums[i] == 6:
        ignore = True
      else:
        sum += nums[i]
      
    i += 1
    
  return sum
