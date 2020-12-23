class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        if not nums1 or not nums2:
            return []

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        return [num for num in set(nums1) if num in set(nums2)]