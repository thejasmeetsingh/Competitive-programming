from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list) -> bool:
        if not arr:
            return False
        counter_values = list(Counter(arr).values())
        return len(counter_values) == len(set(counter_values))