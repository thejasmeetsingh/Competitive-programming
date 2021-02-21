class Solution:
    def findMaxLength(self, nums: list) -> int:
        if not nums:
            return 0

        d = {0: -1}
        max_len, count = 0, 0

        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count in d:
                max_len = max(max_len, i - d[count])
            else:
                d[count] = i

        return max_len