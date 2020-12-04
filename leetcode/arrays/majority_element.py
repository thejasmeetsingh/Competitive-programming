class Solution:
    def majorityElement(self, nums: list) -> int:
        return sorted(nums)[len(nums)//2]