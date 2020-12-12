from bisect import bisect_right


class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        if not nums:
            return 0

        diff = float('inf')
        nums.sort()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = target - nums[i] - nums[j]
                hi = bisect_right(nums, complement, j + 1)
                lo = hi - 1
                if hi < len(nums) and abs(complement - nums[hi]) < abs(diff):
                    diff = complement - nums[hi]
                if lo > j and abs(complement - nums[lo]) < abs(diff):
                    diff = complement - nums[lo]
            if diff == 0:
                break

        return target - diff