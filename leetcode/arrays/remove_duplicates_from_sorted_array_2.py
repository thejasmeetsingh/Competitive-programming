class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if not nums:
            return 0

        if len(nums) < 3:
            return len(nums)
        i = 2
        while i < len(nums):
            if nums[i] == nums[i - 2]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)