class Solution:
    def summaryRanges(self, nums: list) -> list:
        if not nums:
            return nums

        range_list = []
        i = 0

        while i < len(nums):
            j = nums[i]
            count = 0

            while (j + 1) in nums[i:]:
                j += 1
                count += 1

            range_list.append(str(nums[i]) if count == 0 else f"{nums[i]}->{j}")
            i += (count + 1)

        return range_list

