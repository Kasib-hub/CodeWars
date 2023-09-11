// filter out all the strings from a list of objects

import java.util.List;
import java.util.ArrayList;

public class Kata {
  
  public static List<Object> filterList(final List<Object> list) {
    // Return the List with the Strings filtered out
    List<Object> res = new ArrayList<>();
    for (int i = 0; i < list.size(); i++) {
      if (list.get(i) instanceof Integer) res.add(list.get(i));
    }
    return res;
  }
}