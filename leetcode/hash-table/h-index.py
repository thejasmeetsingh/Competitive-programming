class Solution:
    def hIndex(self, citations: list) -> int:
        if not citations:
            return 0

        citations.sort()
        n = len(citations)

        for i in range(n):
            if citations[i] >= n - i:
                return n - i

        return 0
