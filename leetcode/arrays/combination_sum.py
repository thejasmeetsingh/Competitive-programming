class Solution:
    def combinationSum(self, candidates, target) -> list:
        dp = [[] for _ in range(target + 1)]

        for c in candidates:
            for i in range(target + 1):
                if i < c:
                    continue
                if i == c:
                    dp[i].append([c])
                else:
                    for sub_list in dp[i - c]:
                        dp[i].append(sub_list + [c])

        return dp[target]