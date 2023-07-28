public class VowelCount {
  // this is my function?
  // public static data type function parameter
  public static int getCount(String str) {
    String vowels = "aeiou";
    int vowelCount = 0;

    for (int i = 0; i < str.length(); i++) {
      // you have to "pull" the character out the string
      char ch = str.charAt(i);
      if (vowels.contains(String.valueOf(ch))) {
        vowelCount++;
      }
    }

    return vowelCount;
  }

  // but it has to run off main
  public static void main(String[] args) {
    System.out.println(getCount("abracadabra"));
    getCount("world");
  }
}

// then, in the terminal, run:
// javac VowelCount.java
// java VowelCount
