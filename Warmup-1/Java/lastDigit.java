public boolean lastDigit(int a, int b) {

  a %= 10;
  b %= 10;
  
  return a == b;
}
