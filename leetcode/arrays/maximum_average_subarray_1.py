class Solution:
    def findMaxAverage(self, nums: list, k: int) -> float:
        n = len(nums)
        if not nums or k == 0 or n < k:
            return 0.0

        if k == 1:
            return max(nums)

        if n == k:
            return sum(nums) / n

        _sum = sum(nums[:k])
        max_avg = _sum

        for i in range(k, n):
            _sum += nums[i] - nums[i-k]
            max_avg = max_avg if max_avg > _sum else _sum

        return max_avg / k