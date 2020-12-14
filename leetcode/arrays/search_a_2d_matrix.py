class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        if not matrix:
            return False

        for sub_list in matrix:
            if sub_list and sub_list[0] <= target <= sub_list[-1]:
                break

        if sub_list and target in set(sub_list):
            lo = 0
            hi = len(sub_list) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if sub_list[mid] == target:
                    return True
                elif sub_list[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False