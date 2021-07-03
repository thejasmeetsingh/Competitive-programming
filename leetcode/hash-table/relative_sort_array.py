from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: list, arr2: list) -> list:
        if not arr1:
            return []
        
        if not arr2:
            return arr1
        
        arr1_counter = Counter(arr1)
        result = []
        excluded_elements = []

        for el in arr2:
            if arr1_counter.get(el):
                result.extend([el] * arr1_counter.pop(el))
        
        for key in arr1_counter:
            excluded_elements.extend([key] * arr1_counter[key])
        
        result.extend(sorted(excluded_elements))
        return result
