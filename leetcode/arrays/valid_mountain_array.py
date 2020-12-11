class Solution:
    def validMountainArray(self, arr: list) -> bool:
        n = len(arr)
        if not arr or n < 3:
            return False

        _max = max(arr)

        if _max == arr[0] or _max == arr[-1]:
            return False

        idx = arr.index(_max)

        for i in range(idx-1):
            if arr[i] >= arr[i+1]:
                return False

        for j in range(idx+1, n-1):
            if arr[j] <= arr[j+1]:
                return False

        return True