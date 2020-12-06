class Solution:
    def thirdMax(self, nums: list) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums), reverse=True)
        return nums[0] if len(nums) < 3 else nums[2]