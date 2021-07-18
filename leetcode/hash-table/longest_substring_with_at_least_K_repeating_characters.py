from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_len = 0
        lst = [s]

        while lst:
            new_lst = []
            for sub_s in lst:
                new_sub = sub_s
                for c, n in Counter(new_sub).items():
                    if n < k:
                        new_sub = new_sub.replace(c, "#")
                for new_s in new_sub.split("#"):
                    if new_s:
                        if min(Counter(new_s).values()) >= k:
                            max_len = max(max_len, len(new_s))
                        elif len(new_s) >= k:
                            new_lst.append(new_s)
            lst = new_lst

        return max_len
