class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        if not nums or target not in set(nums):
            return [-1, -1]

        if len(nums) == 1:
            return [0, 0]

        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i] != target:
                i += 1
            if nums[j] != target:
                j -= 1
            if nums[i] == nums[j] == target:
                return [i, j]