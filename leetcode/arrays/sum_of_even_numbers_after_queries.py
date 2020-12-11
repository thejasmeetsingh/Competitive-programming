class Solution:
    def sumEvenAfterQueries(self, A: list, queries: list) -> list:
        if not A:
            return A

        result = []
        _sum = sum([el for el in A if not el % 2])

        for q in queries:
            if not A[q[1]] % 2:
                _sum -= A[q[1]]
            A[q[1]] += q[0]
            if not A[q[1]] % 2:
                _sum += A[q[1]]
            result.append(_sum)

        return result
