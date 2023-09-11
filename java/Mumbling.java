// repeat letters based on index in string
// accum("abcd") -> "A-Bb-Ccc-Dddd"

public class Accumul {
    
    public static String accum(String s) {
      // make an array of the string for iteration
      String[] strArr = s.split("");
      // make an array of the result with the same length as the string
      String[] res = new String[s.length()];
      
      for (int i = 0; i < strArr.length; i++) {
        String temp = ""; // this is the string that will be added to the result array
        temp += strArr[i].toUpperCase(); // add the first letter of the string to the temp string - uppercase
        
        String lowerCase = strArr[i].toLowerCase(); // make a string of the lowercase letter
        temp += lowerCase.repeat(i);
        
        res[i] = temp;
      }
      return String.join("-", res);
     // your code
    }
}