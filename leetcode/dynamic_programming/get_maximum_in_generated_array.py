class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if not n:
            return 0

        arr = [0] * 101
        arr[1] = 1
        _max = 1

        for i in range(2, n + 1):
            if i % 2 == 0:
                arr[i] = arr[i // 2]
            else:
                arr[i] = arr[i // 2] + arr[i // 2 + 1]

            _max = max(_max, arr[i])

        return _max
