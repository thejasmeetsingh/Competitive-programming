class Solution:
    def maxProfit(self, prices: list) -> int:
        if not prices:
            return 0

        _min = 1000000000
        _max = 0

        for price in prices:
            _min = price if price < _min else _min
            _max = (price - _min) if (price - _min) > _max else _max

        return _max
