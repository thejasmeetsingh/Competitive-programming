class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        if not nums or len(nums) == len(set(nums)):
            return False

        d = dict()
        for idx, num in enumerate(nums):
            if num in d and (idx - d[num]) <= k:
                return True
            d[num] = idx

        return False