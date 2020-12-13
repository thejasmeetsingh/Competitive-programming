class Solution:
    def canJump(self, nums: list) -> bool:
        if not nums:
            return False

        position = len(nums) - 1

        for i in range(position, -1, -1):
            if i + nums[i] >= position:
                position = i

        return position == 0