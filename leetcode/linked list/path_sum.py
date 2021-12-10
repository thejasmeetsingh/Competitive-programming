# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
          return False
        
        queue = [[root, targetSum]]
        
        while queue:
          node, _sum = queue.pop(0)
          
          if _sum - node.val == 0 and not node.left and not node.right:
            return True
          
          if node.left:
            queue.append([node.left, _sum - node.val])
          if node.right:
            queue.append([node.right, _sum - node.val])
        
        return False
