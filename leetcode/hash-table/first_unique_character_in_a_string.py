class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        dd = dict()

        for i in range(len(s)):
            if s[i] in dd:
                dd[s[i]]['val'] += 1
            else:
                dd[s[i]] = {'val': 1, 'idx': i}

        for key, value in dd.items():
            if value['val'] == 1:
                return value['idx']

        return -1