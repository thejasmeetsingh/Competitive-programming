from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(set)

    def add_edge(self, src, dest):
        self.graph[src].add(dest)
        self.graph[dest].add(src)

    def dfs_util(self, visited, start):
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                queue.extend(list(self.graph[node]))

    def connected_components(self):
        _max_comp = 0
        _min_comp = len(self.graph)

        while self.graph:
            visited = set()

            self.dfs_util(visited, list(self.graph.keys())[0])

            _max_comp = max(_max_comp, len(visited))
            _min_comp = min(_min_comp, len(visited))

            while visited:
                self.graph.pop(visited.pop(), None)

        return _min_comp, _max_comp


if __name__ == "__main__":
    N = int(input())
    graph = Graph()

    for _ in range(N):
        u, v = list(map(int, input().split()))
        graph.add_edge(u, v)

    min_comp, max_comp = graph.connected_components()
    print(min_comp, max_comp)
