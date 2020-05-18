# We want make a package of goal kilos of chocolate. 
# We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use, assuming we always use big bars before small bars.
# Return -1 if it can't be done.

def make_chocolate(small, big, goal):
  
  maxBigs = goal // 5   #how many bigs fit into the goal

  if big < maxBigs:     #if we actually have less bigs than can fit
    maxBigs = big       #use as many bigs as available
    
  if (5*maxBigs) + small >= goal:   #if bigs available and all smalls sum to goal or over
    return goal - (5*maxBigs)       #return difference in small bars needed to complete
  else:
    return -1                       #otherwise not possible
