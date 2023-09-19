// remove every other element from an array

import java.util.ArrayList;
import java.util.List;

// used list for dynamic size
public class Kata {
  
  public static Object[] removeEveryOther(Object[] arr) {
    // create list to store elements
    List<Object> res = new ArrayList<>();

    // add every other element to list
    for (int i = 0; i < arr.length; i++) {
      if (i % 2 == 0) res.add(arr[i]);
    }
    // convert list to array
    Object[] resArr = res.toArray(new Object[0]);
    return resArr;
  }
}