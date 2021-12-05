class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        hmap = dict()

        for idx in range(len(s)):
            if hmap.get(s[idx]):
                hmap[s[idx]][0] += 1
            else:
                hmap[s[idx]] = [1, idx]

        for value in hmap.values():
            if value[0] == 1:
                return value[1]

        return -1
