class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = triangle[-1]
        for i in reversed(range(len(triangle) - 1)):
            row = [x + min(row[j], row[j + 1]) for j, x in enumerate(triangle[i])]
        return row[0]
