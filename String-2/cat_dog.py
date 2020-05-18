# Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
  
  cats, dogs = 0, 0
  
  for i in range(len(str)-2):
    if str[i] == "c" and str[i+1] == "a" and str[i+2] == "t":
      cats += 1
    elif str[i] == "d" and str[i+1] == "o" and str[i+2] == "g":
      dogs += 1
      
  return cats == dogs
