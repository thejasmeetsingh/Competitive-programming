class Solution:
    def findLengthOfLCIS(self, nums: list) -> int:
        if not nums:
            return 0

        max_count = 0
        count = 0

        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                max_count = max_count if max_count > (count + 1) else (count + 1)
                count = 0
            else:
                count += 1

        return max_count if max_count > (count + 1) else (count + 1)