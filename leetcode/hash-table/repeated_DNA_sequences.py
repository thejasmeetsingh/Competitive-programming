class Solution:
    def findRepeatedDnaSequences(self, s: str) -> set:
        if not s:
            return set()

        l, n = 10, len(s)
        seen, output = set(), set()
        for i in range(n - l + 1):
            tmp = s[i:i + l]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
        return output
