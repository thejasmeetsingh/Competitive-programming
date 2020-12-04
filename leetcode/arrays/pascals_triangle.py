class Solution:
    def generate(self, num_rows: int) -> list:
        if num_rows == 0:
            return []

        triangle = [[1]]

        for i in range(1, num_rows):
            prev_row = triangle[i-1]
            triangle.append([1] + list(map(lambda j: prev_row[j-1] + prev_row[j], range(1, i))) + [1])

        return triangle