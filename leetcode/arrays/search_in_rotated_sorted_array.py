class Solution:
    def search(self, nums: list, target: int) -> int:
        if not nums or target not in set(nums):
            return -1

        for i in range(len(nums)):
            if target == nums[i]:
                return i