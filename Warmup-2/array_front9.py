# Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
# The array length may be less than 4.

def array_front9(nums):
  
  is_9 = False
  
  for num in nums[0:3]:
    if num == 9:
      is_9 = True
      
  return is_9
