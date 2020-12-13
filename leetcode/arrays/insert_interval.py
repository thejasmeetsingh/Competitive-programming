class Solution:
    def insert(self, intervals: list, new_interval: list) -> list:
        if not intervals:
            return [new_interval]

        if not new_interval:
            return intervals

        intervals.append(new_interval)
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            elif interval[1] > merged[-1][1]:
                merged[-1][1] = interval[1]

        return merged