# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
          return None
        
        if q.val < p.val: 
          p, q = q, p
          
        while True:
            if q.val < root.val:
                root = root.left
            
            elif p.val > root.val:
                root = root.right
            
            elif p.val <= root.val <= q.val:
                return root
