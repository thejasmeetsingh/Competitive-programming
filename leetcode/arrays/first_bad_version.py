class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        i, j = 1, n
        
        while i < j:
          mid = (i + j) >> 1
          if isBadVersion(mid):
            j = mid
          else:
            i = mid + 1
        
        return i
        
