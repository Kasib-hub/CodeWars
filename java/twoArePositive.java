public class twoArePositive {
  
  public static boolean twoArePositive(int a, int b, int c) {
    // your code here
    int[] numbers = {a, b, c};
    int posFlag = 0;
    for (int number : numbers) {
      if (number > 0) {
        posFlag++;
      }
    }
    if (posFlag == 2) {
        return true;
      }
    return false;
  }

  public static void main(String[] args) {
    System.out.println(twoArePositive(1, 2, 3));
    System.out.println(twoArePositive(-1, 2, 3));
    System.out.println(twoArePositive(1, -2, 3));
    System.out.println(twoArePositive(1, 2, -3));
    System.out.println(twoArePositive(-1, -2, 3));
    System.out.println(twoArePositive(-1, 2, -3));
    System.out.println(twoArePositive(1, -2, -3));
    System.out.println(twoArePositive(-1, -2, -3));
  }
}