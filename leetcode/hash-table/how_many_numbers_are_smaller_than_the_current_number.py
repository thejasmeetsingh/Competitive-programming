class Solution:
    def smallerNumbersThanCurrent(self, nums: list) -> list:
        if not nums:
            return nums

        temp_nums = nums.copy()
        temp_nums.sort()
        map_sequence = dict()

        for i in range(len(nums)):
            if temp_nums[i] not in map_sequence:
                map_sequence[temp_nums[i]] = len(temp_nums[:i])

        return [map_sequence[el] for el in nums]
