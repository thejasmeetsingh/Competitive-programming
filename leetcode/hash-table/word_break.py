class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        if len(s) == 0:
            return True

        dp = [False for i in range(0, len(s))]
        for i in range(0, len(s)):
            if i == 0:
                for j in range(i, len(s)):
                    if s[i:j + 1] in wordDict:
                        dp[j] = True
            elif dp[i - 1] is True:
                for j in range(i, len(s)):
                    if s[i:j + 1] in wordDict:
                        dp[j] = True

        return dp[-1]