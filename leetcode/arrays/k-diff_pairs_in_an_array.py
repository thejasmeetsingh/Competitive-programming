from collections import Counter


class Solution:
    def findPairs(self, nums: list, k: int) -> int:
        if not nums:
            return 0

        count = 0
        if k:
            _set = set(nums)
            for num in _set:
                if (num + k) in _set:
                    count += 1
        else:
            for value in Counter(nums).values():
                if value > 1:
                    count += 1

        return count