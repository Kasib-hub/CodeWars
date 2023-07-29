// https://www.codewars.com/kata/546e2562b03326a88e000020/train/java

public class SquareDigit {
  public static int squareDigits (int n) {
    String res = "";
    String strngNum = String.valueOf(n);

    // iterate and then convert back to int and square to add to the res
    for (char ch : strngNum.toCharArray()) {
      int digit = Character.getNumericValue(ch);
      int squared = digit * digit;
      res += squared;
    }
    return Integer.parseInt(res);
  }

  public static void main(String[] args) {
    System.out.println(squareDigits(9));
  }
}