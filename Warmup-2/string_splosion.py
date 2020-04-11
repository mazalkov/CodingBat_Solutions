# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  
  newString = ""
  
  for i in range(len(str)):
    newString = newString + str[:i+1]
    
  return newString
