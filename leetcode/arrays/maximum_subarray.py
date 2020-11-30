class Solution:
    def maxSubArray(self, nums: list) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        max_curr = 0
        max_global = -(10 ^ 4)

        for num in nums:
            max_curr = max_curr + num
            max_global = max(max_global, max_curr)
            max_curr = 0 if max_curr < 0 else max_curr

        return max_global