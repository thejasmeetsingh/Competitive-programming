from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        most_commons = Counter(s).most_common()
        return "".join(map(lambda x: x[0]*x[1], most_commons))
