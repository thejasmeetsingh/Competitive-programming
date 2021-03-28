class Solution:
    def prisonAfterNDays(self, cells: list, n: int) -> list:

        def helper(cells):
            res = [0] * len(cells)
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    res[i] = 1
            return res

        memo = dict()
        for i in range(1, n + 1):
            cells = helper(cells)
            if i > 1 and cells == memo[1]:
                cycle_n = i - 1
                break
            memo[i] = cells
        else:
            return memo[i]

        if n % cycle_n == 0:
            return memo[cycle_n]
        else:
            return memo[n % cycle_n]