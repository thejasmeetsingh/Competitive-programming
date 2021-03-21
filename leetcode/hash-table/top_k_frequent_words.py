from collections import Counter


class Solution:
    def topKFrequent(self, words: list, k: int) -> list:
        words.sort()
        return list(map(lambda x: x[0], Counter(words).most_common(k)))
