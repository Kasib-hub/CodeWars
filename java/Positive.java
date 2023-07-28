public class Positive {
  public static int sum(int[] arr) {
    int res = 0;
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] > 0) {
        res += arr[i];
      }
    }
    return res;
  }

  public static void main(String[] args) {
    System.out.println(sum(new int[]{1,2,3,4,5}));
    System.out.println(sum(new int[]{1,-2,3,4,5}));
  }
}