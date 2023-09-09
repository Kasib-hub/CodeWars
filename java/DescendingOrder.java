/* 
Convert number to reversed array of digits
*/

import java.util.Arrays;
import java.util.Collections;

public class DescendingOrder {
    public static int sortDesc(final int num) {
        // initialize String array with each digit of num and converting to String
        // the numbers are chained with split.
        String[] array = String.valueOf(num).split("");

        // sort the array in reverse order
        Arrays.sort(array, Collections.reverseOrder());

        // join the array and convert to int
        return Integer.valueOf(String.join("", array));
    }
}