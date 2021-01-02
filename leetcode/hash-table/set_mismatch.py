class Solution:
    def findErrorNums(self, nums: list) -> list:
        if not nums:
            return []

        n, total, total_unique = len(nums), sum(nums), sum(set(nums))
        return [total - total_unique, (1+n) * n//2 - total_unique]