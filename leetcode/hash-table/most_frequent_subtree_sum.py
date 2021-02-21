class Solution:
    def __init__(self):
        self.f = 0
        self.d = dict()

    def findFrequentTreeSum(self, root):
        if not root:
            return []

        def dfs(n):
            s = 0
            if n:
                s = n.val + dfs(n.left) + dfs(n.right)
                self.d[s] = self.d.get(s, 0) + 1
                self.f = max(self.f, self.d[s])
            return s

        dfs(root)
        return [k for k, v in self.d.items() if v == self.f]