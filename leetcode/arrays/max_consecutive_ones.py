class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        if not nums:
            return 0

        count, _max = 0, 0
        for num in nums:
            if num != 1:
                _max = _max if _max > count else count
                count = 0
            else:
                count += 1
        return _max if _max > count else count