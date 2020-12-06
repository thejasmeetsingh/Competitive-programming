class Solution:
    def matrixReshape(self, nums: list, r: int, c: int) -> list:
        rows = len(nums)
        columns = len(nums[0])

        if (rows * columns) != (c * r):
            return nums

        nums = [nums[i][j] for j in range(columns) for i in range(rows)]
        result = []
        for i in range(0, len(nums), c):
            result.append(nums[i:i + c])

        return result