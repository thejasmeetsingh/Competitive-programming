class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if not nums or len(nums) == 1:
          return
        
        last_zero_idx = 0
        curr = 0
        
        while curr < len(nums):
          if nums[curr] != 0:
            nums[last_zero_idx], nums[curr] = nums[curr], nums[last_zero_idx]
            last_zero_idx += 1
            
          curr += 1
