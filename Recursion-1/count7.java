public int count7(int n) {
  int count = 0;
  
  if (n % 10 == 7)
    count = 1;
    
  if (n / 10 == 0)
    return count;
    
  return count + count7(n / 10);
}
