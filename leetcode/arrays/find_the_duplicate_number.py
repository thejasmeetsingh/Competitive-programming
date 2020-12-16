class Solution:
    def findDuplicate(self, nums: list) -> int:
        if not nums:
            return 0

        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]

        return 0