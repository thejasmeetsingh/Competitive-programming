class Solution:
    def countLargestGroup(self, n: int) -> int:
        if n == 0:
            return 0
        
        _dict = dict()

        for i in range(1, n+1):
            _sum = sum([int(char) for char in str(i)])
            if _sum in _dict:
                _dict[_sum].append(i)
            else:
                _dict[_sum] = [i]

        result = sorted([len(_dict[key]) for key in _dict])
        return result.count(result[-1])
