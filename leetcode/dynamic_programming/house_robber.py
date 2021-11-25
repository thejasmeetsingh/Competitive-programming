class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
          return 0
        
        if len(nums) in {1, 2}:
          return max(nums)
        
        a, b = 0, 0
        
        for idx in range(len(nums)):
          a, b = b, max(nums[idx] + a, b)
        
        return b
