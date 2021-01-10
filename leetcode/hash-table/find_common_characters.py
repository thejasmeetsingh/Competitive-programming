from collections import Counter


class Solution:
    def commonChars(self, A: list) -> list:
        c = A[0]
        for i in range(1, len(A)):
            c = list((Counter(c) & Counter(A[i])).elements())
        return c