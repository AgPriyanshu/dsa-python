# Given the head of a singly linked list representing a positive integer number. Each node of the linked list represents a digit of the number, with the 1st node containing the leftmost digit of the number and so on. The task is to add one to the value represented by the linked list and return the head of a linked list containing the final value.
# The number will contain no leading zeroes except when the value represented is zero itself.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

