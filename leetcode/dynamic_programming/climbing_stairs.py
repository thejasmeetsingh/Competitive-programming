class Solution:
    def climbStairs(self, n: int) -> int:
      if n == 0 or n == 1 or n == 2 or n == 3:
        return n
      
      a = 3
      b = 2
      
      for _ in range(4, n + 1):
        a, b = a + b, a
      
      return a
