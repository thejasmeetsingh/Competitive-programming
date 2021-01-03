from collections import Counter


class Solution:
    def uncommonFromSentences(self, string1: str, string2: str) -> list:
        result = list()

        counter = Counter(string1.split(" "))
        counter += Counter(string2.split(" "))

        return [string for string in counter if counter[string] == 1]