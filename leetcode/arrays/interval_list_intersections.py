class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        intervals = []
        
        while i < len(A) and j < len(B):
            interval_starting, interval_end = max(A[i][0], B[j][0]), min(A[i][1], B[j][1])
            
            if interval_starting <= interval_end:
                intervals.append([interval_starting, interval_end])
            
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        
        return intervals
