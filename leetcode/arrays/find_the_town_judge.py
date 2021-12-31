class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a = [0] * n
        b = [0] * n
        
        for t in trust:
            a[t[0]-1] += 1
            b[t[1]-1] += 1
        
        for i in range(n):
            if b[i] == n - 1 and a[i] == 0:
                return i + 1
              
        return -1
        
