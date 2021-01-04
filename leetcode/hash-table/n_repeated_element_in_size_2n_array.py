from collections import Counter


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        if not A:
            return 0
        
        _set = set()
        
        for el in A:
            if el in _set:
                return el
            _set.add(el)
        
        return 0
