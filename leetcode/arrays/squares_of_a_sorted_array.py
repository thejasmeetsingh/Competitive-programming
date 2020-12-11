class Solution:
    def sortedSquares(self, nums: list) -> list:
        if not nums:
            return nums

        for i in range(len(nums)):
            nums[i] **= 2

        nums.sort()
        return nums