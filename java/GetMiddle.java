  public static String getMiddle(String word) {
    String res = "";
    int length = word.length();
    int middle = length / 2;
    
    // if the length of the word is even, return the middle two characters
    if (length % 2 == 0) res = word.substring(middle - 1, middle + 1);
    
    // if the length of the word is odd, return the middle character
    else res = word.substring(middle, middle + 1);
    
    return res;
    //Code goes here!
  }