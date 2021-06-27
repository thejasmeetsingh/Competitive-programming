class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False

        _dict = {}
        q = list()
        q.append(root)

        while q:
            node = q.pop(0)

            if node.val in _dict:
                return True
            else:
                _dict[k - node.val] = node.val

            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
        
        return False

