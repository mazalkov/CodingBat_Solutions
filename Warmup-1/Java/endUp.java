public String endUp(String str) {
  int LENGTH = str.length();
  if (LENGTH >= 3) {
   return str.substring(0, LENGTH-3) + str.substring(LENGTH-3).toUpperCase(); 
  }
  return str.toUpperCase();
}
