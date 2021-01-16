class Solution:
    def numIdenticalPairs(self, nums: list) -> int:
        if not nums:
            return 0

        count = 0
        for i in range(len(nums)-1):
            count += nums[i+1:].count(nums[i])

        return count