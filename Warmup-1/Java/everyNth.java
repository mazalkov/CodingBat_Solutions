public String everyNth(String str, int n) {
  
  if (n > str.length()) {
    return String.valueOf(str.charAt(0));
  }
  
  StringBuilder result = new StringBuilder();
  
  for (int i = 0; i <= str.length()-1; i += n) {
    result.append(str.charAt(i));
  }
  
  return result.toString();
}
