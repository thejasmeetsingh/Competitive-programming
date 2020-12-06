class Solution:
    def imageSmoother(self, M: list) -> list:
        m, n = len(M), len(M[0])

        sums = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                sums[r][c] = sum(M[r][max(0, c - 1):c + 2])

        for r in range(m):
            for c in range(n):
                total = sums[r][c]
                sum_count = 3 if c != 0 and c != n - 1 else min(n, 2)
                total_count = sum_count

                if r != 0:
                    total += sums[r - 1][c]
                    total_count += sum_count

                if r != m - 1:
                    total += sums[r + 1][c]
                    total_count += sum_count

                M[r][c] = total // total_count

        return M