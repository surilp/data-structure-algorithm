from collections import deque


class Graph:

    def __init__(self, n, edges, directed=False, zero_based=False):
        self.n = n
        self.zero_based = zero_based
        self.edges = edges
        self.adj_list = Graph.get_adj_list(n, edges, directed, zero_based)

    @staticmethod
    def get_adj_matrix(n, edges, directed=False, zero_based=False):
        if not zero_based:
            n = n + 1
        matrix = [[None] * (n) for _ in range(n)]
        for edge in edges:
            from_v = edge[0]
            to_v = edge[1]
            weight = 1 if len(edge) < 3 else edge[2]
            matrix[from_v][to_v] = weight
            if not directed:
                matrix[to_v][from_v] = weight
        return matrix

    @staticmethod
    def get_adj_list(n, edges, directed=False, zero_based=False):
        if not zero_based:
            n = n + 1
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            from_v = edge[0]
            to_v = edge[1]
            weight = None if len(edge) < 3 else edge[2]
            if weight:
                temp = [to_v, weight]
            else:
                temp = to_v
            adj_list[from_v].append(temp)
            if not directed:
                adj_list[to_v].append(temp)
        return adj_list

    def dfs(self):
        n = self.n if self.zero_based else self.n + 1
        start = 0 if self.zero_based else 1
        result = []
        visited = [False] * n
        for vertex in range(start, n):
            if not visited[vertex]:
                self._dfs(vertex, visited, result)
        return result

    def _dfs(self, vertex, visited, result):
        visited[vertex] = True
        result.append(vertex)
        for adj_vertex in self.adj_list[vertex]:
            if not visited[adj_vertex]:
                self._dfs(adj_vertex, visited, result)
        return result

    def bfs(self):
        n = self.n if self.zero_based else self.n + 1
        start = 0 if self.zero_based else 1
        result = []
        visited = [False] * n
        for vertex in range(start, n):
            if not visited[vertex]:
                self._bfs(vertex, visited, result)
        return result

    def _bfs(self, start, visited, result):
        queue = deque()
        queue.append(start)
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            visited[vertex] = True
            for adj_vertex in self.adj_list[vertex]:
                if not visited[adj_vertex]:
                    queue.append(adj_vertex)
        return result
