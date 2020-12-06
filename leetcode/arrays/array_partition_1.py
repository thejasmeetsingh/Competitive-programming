class Solution:
    def arrayPairSum(self, nums: list) -> int:
        if not nums:
            return 0
        nums.sort()
        return sum([nums[i] for i in range(0, len(nums), 2)])