public boolean stringE(String str) {
  int count = str.length() - str.replace("e", "").length();
  
  return (1 <= count) && (count <=3);
}
