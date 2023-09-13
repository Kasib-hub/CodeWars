// how long will it take the 2nd tortoise to catch up to the 1st tortoise with a headstart? G is the headstart in meters, v1 and v2 are the speeds of the tortoises in meters per hour. Return an array [hours, minutes, seconds] or null if v2 <= v1

public class Tortoise {
    public static int[] race(int v1, int v2, int g) {
      int totalSeconds = 0;
      
      if (v2 > v1) totalSeconds = (g * 3600) / (v2 - v1);
      else return null;
      
      // hours calculated by dividing total seconds by 3600
      int hours = totalSeconds / 3600;

      // minutes calculated by dividing the remainder of total seconds divided by 3600 by 60
      int minutes = (totalSeconds % 3600) / 60;

      // seconds calculated by dividing the remainder of total seconds divided by 3600 by 60
      int seconds = totalSeconds % 60;
        
      int[] res = {hours, minutes, seconds};
      return res;
    }
}