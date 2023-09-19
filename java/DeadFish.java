// given string of commands, return array of values. Commands given are:
// i - increment value
// d - decrement value
// s - square value
// o - output value

// couldn't convert Integer[] to int[] so used Object[] instead 
// it should use streams to convert but I don't know how to use streams yet

import java.util.ArrayList;
import java.util.List;

public class DeadFish {
    public static int[] parse(String data) {
      String[] arr = data.split("");
      
      // create the list to store elements dynamically
      List<Object> tempRes = new ArrayList<>();
      
      // iterate through data
      int value = 0;
      
      // == tests exact object ref not value so use .equals()
      for (String letter : arr) {
        if (letter.equals("i")) value++;
        else if (letter.equals("d")) value--;
        else if (letter.equals("s")) value *= value;
        else if (letter.equals("o")) {
          tempRes.add(value);
        }
      }
      
      // convert back to int array
      Object[] objTempRes = tempRes.toArray(new Object[0]);
      int[] res = new int[objTempRes.length];
      
      for (int i = 0; i < objTempRes.length; i++) {
        res[i] = (int) objTempRes[i];  
      }
      
      return res;
        // Implement me! :)
    }
}