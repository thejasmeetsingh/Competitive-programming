class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = dict()
        values = set()

        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] in d:
                    if d[s[i]] != t[i]:
                        return False
                else:
                    if t[i] in values:
                        return False
                    d[s[i]] = t[i]
                    values.add(t[i])

        return True