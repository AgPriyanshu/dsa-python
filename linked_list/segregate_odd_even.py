# Given the head of a singly linked list. Group all the nodes with odd indices followed by all the nodes with even indices and return the reordered list.
# Consider the 1st node to have index 1 and so on. The relative order of the elements inside the odd and even group must remain the same as the given input.

class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next

class Solution:
    def oddEvenList(self, head):
      """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
      """
      counter = 1
      current = head
      odd_place_pointer = None

      if head.next is None:
        return
      
      while current != None:
          if odd_place_pointer is not None and (counter % 2) != 0:
            temp = odd_place_pointer.data
            odd_place_pointer.data = current.data
            current.data = temp
            odd_place_pointer = current

          counter += 1
          current = current.next
      
      return head