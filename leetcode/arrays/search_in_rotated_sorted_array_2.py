class Solution:
    def search(self, nums: list, target: int) -> bool:
        if not nums:
            return False

        n = len(nums)

        if n < 10:
            return target in set(nums)

        i = 1
        while i < n - 1:
            if nums[i] < nums[i-1]:
                break
            i += 1

        left = 0
        right = n - 1

        if nums[left] <= target <= nums[i-1]:
            right = i - 1
        else:
            left = i

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False