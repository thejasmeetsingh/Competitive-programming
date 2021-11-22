"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
          return None
        
        curr_node = root
        queue = [curr_node]
        
        while queue:
          length = len(queue)
          prev_node = queue.pop(0)
          
          if prev_node.left:
            queue.append(prev_node.left)
          if prev_node.right:
            queue.append(prev_node.right)
          
          for _ in range(length - 1):
            node = queue.pop(0)
            prev_node.next = node
            
            if node.left:
              queue.append(node.left)
            if node.right:
              queue.append(node.right)
            
            prev_node = node
            
        return root
