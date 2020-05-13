# We want to make a row of bricks that is goal inches long. 
# We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
# Return True if it is possible to make the goal by choosing from the given bricks. 
# This is a little harder than it looks and can be done without any loops.

def make_bricks(small, big, goal):
  
  if (goal % 5 == 0) and (big >= (goal / 5)):
    return True

  elif (big >= (goal // 5)) and (small >= (goal % 5)):
    return True
    
  elif (small >= (goal - 5*big)) and ((goal - 5*big) >= 0):
    return True
  
  else:
    return False
    
    
