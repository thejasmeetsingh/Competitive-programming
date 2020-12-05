class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        idx1, idx2 = 0, 1
        while idx2 < len(nums):
            if nums[idx1] != 0:
                idx1 += 1
                idx2 += 1
            else:
                if nums[idx2] != 0:
                    c = nums[idx1]
                    nums[idx1] = nums[idx2]
                    nums[idx2] = c
                else:
                    idx2 += 1