# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
  
  appears = False
  
  for i in range((len(nums)-2)):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      appears = True
      
  return appears
