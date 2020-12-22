from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [False]*2 + [True]*(n-2)
        for i in range(2, int(sqrt(n))+1):
            if primes[i]:
                for k in range(i*i, n, i):
                    primes[k] = False
        return sum(primes)