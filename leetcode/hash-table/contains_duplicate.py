class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        return len(nums) == len(set(nums))