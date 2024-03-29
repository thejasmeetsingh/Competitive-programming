# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA:
          return headB
        
        if not headB:
          return headA
        
        node1 = headA
        node2 = headB
        
        while node1 != node2:
          node1 = node1.next if node1 else headB
          node2 = node2.next if node2 else headA
        
        return node1
