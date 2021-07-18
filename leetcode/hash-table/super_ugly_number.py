import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list) -> int:
        if not primes:
            return 0

        nums = primes.copy()
        heapq.heapify(nums)
        el = 1

        for i in range(n - 1):
            el = heapq.heappop(nums)
            for prime in primes:
                heapq.heappush(nums, el * prime)
                if el % prime == 0:
                    break

        return el
