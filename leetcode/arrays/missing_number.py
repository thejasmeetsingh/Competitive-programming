class Solution:
    def missingNumber(self, nums: list) -> int:
        return ((len(nums) + len(nums) + 1) // 2) - sum(nums)