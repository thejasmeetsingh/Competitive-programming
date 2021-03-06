class Solution:
    def threeSum(self, nums: list) -> list:
        lookup = {}
        res = set()
        nums.sort()

        for i, each in enumerate(nums):
            lookup[each] = i

        for i, a in enumerate(nums):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j, b in enumerate(nums[i + 1:]):
                c = -(a + b)
                if c in lookup and lookup[c] > i and lookup[c] > j + i + 1:
                    res.add((a, b, c))
        return list(res)