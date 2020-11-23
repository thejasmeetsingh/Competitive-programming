class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        d = dict()

        for idx, num in enumerate(nums):
            if (target - num) in d:
                return [d[target - num], idx]
            d[num] = idx

        return []
