import java.util.ArrayList;

public class MultipleIndex {
  public static int[] multipleOfIndex(int[] array) {
    ArrayList<Integer> intArr = new ArrayList<>();
    
    for (int i = 0; i < array.length; i++) {
      if (i == 0) {
        if (array[i] == 0) {
        intArr.add(0);
        } 
      } else {
        if (array[i] % i == 0) intArr.add(array[i]);
      } 
    }
    System.out.println(intArr.size());
    int[] res = new int[intArr.size()];
    for (int i = 0; i < intArr.size(); i++) {
      res[i] = intArr.get(i);
    }
    
    return res;
  }
}