# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if not head or not head.next:
        return head
      
      prev = None
      curr = head
      new_head = None
      
      while curr and curr.next:
          tmp = curr.next
          curr.next = tmp.next
          tmp.next = curr
          
          if not new_head:
            new_head = tmp
          else:
            prev.next = tmp
          
          prev = curr
          curr = curr.next

      return new_head
