public String front22(String str) {
  String front;
  int LENGTH = Math.min(2, str.length());
  front = str.substring(0, LENGTH);
  return front + str + front;
}
