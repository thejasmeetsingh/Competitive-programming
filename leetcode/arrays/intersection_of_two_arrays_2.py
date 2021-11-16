import collections

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        result = []
        
        if len(nums1) >= len(nums2):
            nums1, nums2 = collections.Counter(nums1), nums2
        else:
            nums1, nums2 = collections.Counter(nums2), nums1
            
        for num in nums2:
            if nums1.get(num, 0) > 0:
                nums1[num] -= 1
                result.append(num)
                
        return result
