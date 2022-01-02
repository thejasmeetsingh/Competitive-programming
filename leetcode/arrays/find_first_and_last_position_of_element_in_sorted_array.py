class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
          return [-1, -1]
        
        if len(nums) == 1:
          if target == nums[0]:
            return [0, 0]
          else:
            return [-1, -1]
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
          if nums[low] != target:
            low += 1
          
          if nums[high] != target:
            high -= 1
          
          if nums[low] == nums[high] == target:
            return [low, high]
        
        return [-1, -1]
