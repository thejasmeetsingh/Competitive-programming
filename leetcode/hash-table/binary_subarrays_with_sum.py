class Solution:
    def numSubarraysWithSum(self, arr: list, _sum: int) -> int:
        if not arr:
            return 0

        j, k = 0, 0
        thresh_sum = 0
        count = 0

        for i, el in enumerate(arr):
            thresh_sum += el

            while j < i and thresh_sum > _sum:
                thresh_sum -= arr[j]
                j += 1

            k = j

            while k < i and not arr[k]:
                k += 1

            if thresh_sum == _sum:
                count += k - j + 1

        return count
