class Solution:
    def maxProduct(self, nums: list) -> int:
        Gmax = Cmax = Cmin = nums[0]
        for i in range(1, len(nums)):
            curMax = Cmax
            Cmax = max(Cmax * nums[i], nums[i], Cmin * nums[i])
            Cmin = min(curMax * nums[i], nums[i], Cmin * nums[i])
            Gmax = max(Gmax, Cmax)
        return Gmax