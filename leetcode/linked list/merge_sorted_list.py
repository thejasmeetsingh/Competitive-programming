# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
          return l2
        
        if not l2:
          return l1
        
        node1 = l1
        node2 = l2
        
        node3_root = ListNode()
        node3 = node3_root
        
        while node1 or node2:
          if (node1 and node2 and node1.val < node2.val) or (node1 and node2 is None):
            node3.next = ListNode(val=node1.val)
            node1 = node1.next
            node3 = node3.next
          elif node2:
            node3.next = ListNode(val=node2.val)
            node2 = node2.next
            node3 = node3.next
          
        return node3_root.next
