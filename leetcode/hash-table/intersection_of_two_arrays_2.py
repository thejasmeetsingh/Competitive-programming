from collections import Counter


class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        if not nums1 or not nums2:
            return []

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        nums1_counter = Counter(nums1)
        nums2_counter = Counter(nums2)

        result = []

        for key, value in nums1_counter.items():
            if key in nums2_counter and nums2_counter[key] != 0:
                result = result + [key] * (nums2_counter[key] if nums2_counter[key] < value else value)
                nums2_counter[key] -= 1

        return result