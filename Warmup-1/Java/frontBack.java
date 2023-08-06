public String frontBack(String str) {
  int length = str.length();
  if (length <= 1) {
    return str;
  }
  return str.charAt(length - 1) + str.substring(1, length - 1) + str.charAt(0); 
}
