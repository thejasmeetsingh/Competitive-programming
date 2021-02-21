class Solution:
    def fourSumCount(self, A: list, B: list, C: list, D: list) -> int:
        hm = dict()
        result = 0

        for a in A:
            for b in B:
                hm[a+b] = hm.get(a+b, 0) + 1

        for c in C:
            for d in D:
                result += hm.get(-(c+d), 0)

        return result