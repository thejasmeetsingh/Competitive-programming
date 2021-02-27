class Solution:
    def subarraySum(self, nums: list, k: int, count=0, curr_sum=0) -> int:
        if not nums:
            return 0

        d = {0: 1}
        for el in nums:
            curr_sum += el
            key = curr_sum - k
            if key in d:
                count += d[key]
            d[curr_sum] = d.get(curr_sum, 0) + 1

        return count