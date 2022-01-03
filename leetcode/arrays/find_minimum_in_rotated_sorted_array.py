class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
          return -1
        
        if nums[0] < nums[-1]:
          return nums[0]
        
        for idx in range(len(nums) - 1):
          if nums[idx] > nums[idx + 1]:
            return nums[idx + 1]
        
        return nums[0]
