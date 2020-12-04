class Solution:
    def getRow(self, row_index: int) -> list:
        if row_index == 0:
            return [1]

        triangle = [1] * (row_index + 1)

        for i in range(1, row_index + 1):
            start = triangle[0]
            end = triangle[-1]
            for j in range(1, i):
                triangle[j] = start + end
                start = end
                end = triangle[j + 1]

        return triangle