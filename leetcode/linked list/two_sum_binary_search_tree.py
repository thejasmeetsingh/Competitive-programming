# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
          return False
        
        visited = set()
        queue = [root]
        
        while queue:
          node = queue.pop(0)
          
          if k - node.val in visited:
            return True
          else:
            visited.add(node.val)
          
          if node.left:
            queue.append(node.left)
          if node.right:
            queue.append(node.right)
        
        return False
