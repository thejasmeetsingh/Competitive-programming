class Solution:
    def checkPossibility(self, nums: list) -> bool:
        if not nums:
            return False

        idx, changed, n = 0, False, len(nums)

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if not changed:
                    idx = i
                    changed = True
                else:
                    return False

        return (n <= 3 or changed is False or idx == 0 or idx == (n - 2)) or (
                idx > 0 and nums[idx - 1] <= nums[idx + 1]) or \
               (0 < idx < (n - 2) and nums[idx] <= nums[idx + 2])
