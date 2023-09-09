// spinning words that are 5 or more characters long in reverse order, all other words are left alone

import java.util.Arrays;

public class SpinWords {

  public String spinWords(String sentence) {

    // split the sentence into an array of words
    String[] words = sentence.split(" ");

    // loop through the array of words
    for (int i = 0; i < words.length; i++) { 

      // if the word is 5 or more characters long, reverse it
      if (words[i].length() >= 5) {

        // convert the word to a StringBuilder object, reverse it, and convert back to a String
        words[i] = new StringBuilder(words[i]).reverse().toString();
      }
    }
    // join the array of words into a sentence
    return String.join(" ", words);
  }
}