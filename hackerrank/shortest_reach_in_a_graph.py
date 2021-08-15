class Graph:
    def __init__(self, total_nodes, weight=6):
        self.graph = {node: set() for node in range(1, total_nodes+1)}
        self.weight = weight

    def add_edge(self, src, dest):
        self.graph[src].add(dest)
        self.graph[dest].add(src)

    def find_all_distances(self, _start_node):
        _distances = {x: -1 for x in range(1, n+1)}
        queue = [(_start_node, 0)]

        while queue:
            node, distance = queue.pop(0)
            if _distances[node] < 0:
                _distances[node] = distance
                queue.extend([(node, distance + 6) for node in self.graph[node]])

        return _distances


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        n, m = list(map(int, input().split()))
        graph = Graph(n)

        for __ in range(m):
            u, v = list(map(int, input().split()))
            graph.add_edge(u, v)

        start_node = int(input())
        distances = graph.find_all_distances(start_node)
        print(' '.join([str(distances[distance]) for distance in distances if distances[distance] != 0]))
