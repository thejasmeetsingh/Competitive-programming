# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      if not l1:
        return l2
      
      if not l2:
        return l1
      
      node1 = l1
      node2 = l2
      new_head = ListNode()
      curr_node = new_head
      carry = 0
      
      while node1 or node2:
        x = node1.val if node1 else 0
        y = node2.val if node2 else 0
        
        _sum = carry + x + y
        carry = _sum // 10
        
        curr_node.next = ListNode(_sum % 10)
        curr_node = curr_node.next
        
        if node1:
          node1 = node1.next
        if node2:
          node2 = node2.next
      
      if carry > 0:
        curr_node.next = ListNode(carry)
      
      return new_head.next
