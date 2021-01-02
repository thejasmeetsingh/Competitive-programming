class Solution:
    def findLHS(self, nums: list) -> int:
        if not nums:
            return 0

        d = dict()
        result = 0

        for num in nums:
            d[num] = d.get(num, 0) + 1

            if (num + 1) in d:
                result = max(result, d.get(num) + d.get(num+1))
            if (num - 1) in d:
                result = max(result, d.get(num) + d.get(num - 1))

        return result