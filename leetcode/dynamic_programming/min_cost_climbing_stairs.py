class Solution(object):
    def minCostClimbingStairs(self, cost):
        f1 = f2 = 0
        for x in cost[::-1]:
            f1, f2 = x + (f1 if f1 < f2 else f2), f1
        return f1 if f1 < f2 else f2
