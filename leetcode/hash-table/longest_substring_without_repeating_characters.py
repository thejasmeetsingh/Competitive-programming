class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        sub = ""
        max_len, cur_len = [0, 0]

        for ch in s:
            if ch in sub:
                index = sub.index(ch)
                sub = sub[index + 1:]
                cur_len = len(sub)
            sub += ch
            cur_len += 1
            if max_len < cur_len:
                max_len = cur_len

        return max_len