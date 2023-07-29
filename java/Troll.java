// https://www.codewars.com/kata/52fba66badcd10859f00097e/solutions/java

public class Troll {
  public static String disemvowel(String str) {
    String vowels = "aeiouAEIOU";
    String res = "";

  // iterate through the words, then go through each character and build the result from there
    String ans = str.replaceAll("[aeiouAEIOU]", "");
    return ans;
  }

  public static void main(String[] args) {
    System.out.println(disemvowel("What are you doing lad?"));
  }
}