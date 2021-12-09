# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
          return False
        
        queue = [[root, root]]
        
        while queue:
            node1, node2 = queue.pop(0)
            
            if not node1 and not node2: 
                continue
                
            if not node1 or not node2:
                return False
              
            if node1.val != node2.val:
                return False
        
            queue.append([node1.left, node2.right])
            queue.append([node1.right, node2.left])
        
        return True 
