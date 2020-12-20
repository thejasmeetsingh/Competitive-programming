class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        v2e = v1e = 0
        v2h = v1h = float('-inf')

        for p in prices:
            v2e = max(v2e, v2h + p)
            v2h = max(v2h, v1e - p)
            v1e = max(v1e, v1h + p)
            v1h = max(v1h, - p)

        return v2e