from collections import Counter


class Solution:
    def findLucky(self, arr: list) -> int:
        if not arr:
            return -1
        
        result = []

        for _tuple in Counter(arr).most_common():
            if int(_tuple[0]) == int(_tuple[1]):
                result.append(int(_tuple[0]))
        
        if not result:
            return -1
        
        result.sort()
        return result[-1]
