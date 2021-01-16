class Solution:
    def findKthPositive(self, arr: list, k: int) -> int:
        n = arr[-1] + k
        arr_set = set(arr)
        return list(filter(lambda el: el not in arr_set, range(1, n+1)))[k-1]