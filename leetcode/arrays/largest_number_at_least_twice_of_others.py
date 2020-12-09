class Solution:
    def dominantIndex(self, nums: list) -> int:
        if not nums:
            return -1
        
        large_num = sorted(nums)[-1]
        index = nums.index(large_num)
        nums.pop(index)
        for num in nums:
            if num * 2 > large_num:
                return -1
        
        return index
