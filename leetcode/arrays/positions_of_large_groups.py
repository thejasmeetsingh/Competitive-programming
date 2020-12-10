class Solution(object):
    def largeGroupPositions(self, S) -> list:
        if not S:
            return []

        large_groups = []
        i = 0
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                if j-i+1 >= 3:
                    large_groups.append([i, j])
                i = j+1

        return large_groups