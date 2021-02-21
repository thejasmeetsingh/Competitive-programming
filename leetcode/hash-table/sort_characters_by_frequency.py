class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return s

        counter = dict()
        result = ""

        for char in s:
            counter[char] = counter.get(char, 0) + 1

        for key in sorted(counter, key=lambda x: counter[x], reverse=True):
            result += key * counter[key]
        return result
