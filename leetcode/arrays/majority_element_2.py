from collections import Counter


class Solution:
    def majorityElement(self, nums: list) -> list:
        if not nums:
            return []

        return [key for key, value in Counter(nums).items() if value > len(nums) / 3]
