// https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/solutions/java?filter=me&sort=best_practice&invalids=false

// You are given a node that is the beginning of a linked list. 
// This list always contains a tail and a loop. Find the size of the loop.

public class LoopInspector {

  public int loopSize(Node node) {
    // intialize slow and fast pointers
    Node slow = node;
    Node fast = node;
    
    // move slow and fast pointers
    while (fast != null && fast.getNext() != null) {
      slow = slow.getNext();
      fast = fast.getNext().getNext();
      
      // if slow and fast pointers meet, then there is a loop
      // find the length of the loop by moving slow pointer and counting
      if (slow == fast) {
        int count = 0;
        Node start = slow;

        // move slow pointer and count until it meets start pointer
        while (fast != null && fast.getNext() != null) {
          slow = slow.getNext();
          count++;

          // if slow pointer meets start pointer, then return count
          if (slow == start) return count;
        }
      }
    }
    return 0;
  }
  

}