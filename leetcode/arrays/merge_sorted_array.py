class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        for i, j in zip(range(m, len(nums1)), range(n)):
            nums1[i] = nums2[j]
        nums1.sort()