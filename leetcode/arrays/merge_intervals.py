class Solution:
    def merge(self, intervals: list) -> list:
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            elif interval[1] > merged[-1][1]:
                merged[-1][1] = interval[1]

        return merged