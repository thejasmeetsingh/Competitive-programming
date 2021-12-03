class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        if not matrix:
            return False

        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = (start + end) >> 1
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                if matrix[mid][0] == target or matrix[mid][-1] == target:
                    return True

                _start = 0
                _end = len(matrix[mid]) - 1

                while _start <= _end:
                    _mid = (_start + _end) >> 1
                    if matrix[mid][_mid] == target:
                        return True
                    elif target < matrix[mid][_mid]:
                        _end = _mid - 1
                    else:
                        _start = _mid + 1
                return False
            elif target < matrix[mid][0]:
                end = mid - 1
            else:
                start = mid + 1

        return False
