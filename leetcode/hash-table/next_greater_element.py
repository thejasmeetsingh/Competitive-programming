class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        if not nums1 or not nums2:
            return []
        
        _dict, result = {}, []

        for i in range(len(nums2)-1):
            _dict[nums2[i]] = nums2[i+1:]
        
        for num in nums1:
            if num not in _dict:
                result.append(-1)
            else:
                is_added = False

                for j in range(len(_dict[num])):
                    if _dict[num][j] > num:
                        result.append(_dict[num][j])
                        is_added = True
                        break
                
                if not is_added:
                    result.append(-1)
    
        return result
