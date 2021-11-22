class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or n == 0:
          return head
        
        
        linklist = list()
        curr_node = head
        
        while curr_node:
          linklist.append(curr_node)
          curr_node = curr_node.next
        
        if len(linklist) - n == 0:
          return head.next
        
        node = linklist[-n]
        
        if node.next:
          node.val = node.next.val
          node.next = node.next.next
        else:
          prev_node = linklist[-n-1]
          prev_node.next = None
        
        return head
