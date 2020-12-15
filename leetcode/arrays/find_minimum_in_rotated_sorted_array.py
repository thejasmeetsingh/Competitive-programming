class Solution:
    def findMin(self, nums: list) -> int:
        if not nums:
            return 0

        if nums[-1] > nums[0]:
            return nums[0]

        return min(nums) if nums else 0