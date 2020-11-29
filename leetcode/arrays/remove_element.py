class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        if not nums or val not in nums:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -1

        nums.sort(reverse=True)
        return len(nums[:nums.index(-1)])