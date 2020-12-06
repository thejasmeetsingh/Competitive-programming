class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        if not nums:
            return []
        n = len(nums)
        nums = set(nums)
        return [i for i in range(1, n + 1) if i not in nums]