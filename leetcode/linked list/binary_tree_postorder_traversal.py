# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
          return []
        
        visited = set()
        result, stack = [], []
        node = root
        
        while stack or node:
          if node:
            stack.append(node)
            node = node.left
          else:
            node = stack.pop()
            if node.right and node.right not in visited:
              stack.append(node)
              node = node.right
            else:
              visited.add(node)
              result.append(node.val)
              node = None
            
        return result
