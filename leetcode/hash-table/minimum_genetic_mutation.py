import collections


class Solution:
    def minMutation(self, start: str, end: str, bank: list) -> int:
        graph = {s: collections.Counter([(i, c) for i, c in enumerate(s)]) for s in [start, end] + bank}
        mutation = lambda s, e: sum(((graph[s] | graph[e]) - (graph[s] & graph[e])).values()) == 2
        queue = collections.deque([("", start, 0)])

        while queue:
            prev, s, count = queue.popleft()

            if s == end:
                return count

            for i in bank:
                if i == prev or not mutation(s, i):
                    continue

                queue.append((s, i, count + 1))

        return -1
