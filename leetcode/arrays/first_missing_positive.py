class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        nums.sort()

        if not nums or nums[-1] < 1:
            return 1

        _set = set(nums)
        for i in range(1, nums[-1]+1):
            if i not in _set:
                return i

        return nums[-1]+1