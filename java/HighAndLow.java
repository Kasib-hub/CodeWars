// given a string of space separated numbers, return the highest and lowest number

public class Kata {
  public static String highAndLow(String numbers) {
    // split the string into an array of numbers that are strings
    String[] nums = numbers.split(" ");

    int high = Integer.parseInt(nums[0]);
    int low = Integer.parseInt(nums[0]);

    for (String num : nums) {
      int digit = Integer.parseInt(num);
      if (digit > high) {
        high = digit;
      } else if (digit < low) {
        low = digit;
      }
        
    }
    return String.format("%d %d", high, low);
    }
  }