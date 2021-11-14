class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
          return -1
        
        
        i, j = 0, len(nums)
        
        while i < j:
          mid = (i + j) // 2
          
          if nums[mid] == target:
            return mid
          if nums[mid] < target:
            i = mid + 1
          else:
            j = mid
            
        return i
