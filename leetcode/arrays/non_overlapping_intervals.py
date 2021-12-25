class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 0: 
          return 0
        
        res = 0
        intervals.sort(key=lambda x: x[0])
        
        prev = intervals[0]
        
        for i in range(1, len(intervals)):
          cur = intervals[i]
          if cur[0] < prev[1]:
            res += 1
            prev[1] = min(cur[1], prev[1])
          else:
            prev = cur
          
        return res
