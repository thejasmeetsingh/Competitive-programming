class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        if not nums:
            return nums
        d = dict()
        for num in nums:
            d[num] = d.get(num, 0) + 1
        return sorted(d, key=lambda x: d[x], reverse=True)[:k]
