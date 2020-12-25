from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t

        if not t:
            return ""

        s_counter = Counter(s)
        t_counter = Counter(t)

        for key, value in t_counter.items():
            if key not in s_counter:
                return key
            elif key in s_counter and s_counter[key] < value:
                return key

        return ""
