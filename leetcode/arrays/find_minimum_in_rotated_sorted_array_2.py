class Solution:
    def findMin(self, nums: list) -> int:
        if not nums:
            return 0

        nums.sort()
        return nums[0]
