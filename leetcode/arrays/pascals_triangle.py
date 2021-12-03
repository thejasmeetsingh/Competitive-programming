class Solution:
    def generate(self, numRows: int) -> list:
        if not numRows:
            return []

        if numRows == 1:
            return [[1]]

        triangle = [[1], [1, 1]]

        for i in range(2, numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j >= i:
                    row.append(1)
                elif j < len(triangle[-1]):
                    row.append(triangle[-1][j - 1] + triangle[-1][j])
            triangle.append(row)

        return triangle
