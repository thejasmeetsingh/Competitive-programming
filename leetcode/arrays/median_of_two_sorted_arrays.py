class Solution:
    def get_median(self, data):
        n = len(data)
        if n == 0:
            return 0
        if n % 2 == 1:
            return data[n // 2]
        else:
            i = n // 2
            return (data[i - 1] + data[i]) / 2

    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        if not nums1 or not nums2:
            return self.get_median(nums1) if nums1 else self.get_median(nums2)

        nums1 = nums1 + nums2
        nums1.sort()
        return self.get_median(nums1)