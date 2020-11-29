class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            lo = 0
            hi = len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if target < nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            return lo