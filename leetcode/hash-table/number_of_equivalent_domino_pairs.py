class Solution:
    def numEquivDominoPairs(self, dominoes: list) -> int:
        if not dominoes:
            return 0
        
        _dict = dict()

        for dominoe in dominoes:
            dominoe = tuple(dominoe)

            if dominoe[::-1] in _dict:
                _dict[dominoe[::-1]] += 1
            elif dominoe in _dict:
                _dict[dominoe] += 1
            else:
                _dict[dominoe] = 0
    
        return sum([(i * (i + 1)) // 2 for i in _dict.values()])
