class Solution:
    def climbStairs(self, n: int) -> int:
      if n <= 2:
        return n
      
      a = 1
      b = 2
      
      for i in range(1, n - 1):
        if i % 2 == 1:
          a += b
        else:
          b += a
      
      return a if n % 2 else b
