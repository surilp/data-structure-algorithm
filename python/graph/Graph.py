from collections import deque
from heapq import heappop, heappush, heapify


class Graph:

    def __init__(self, n, edges, directed=False, zero_based=False):
        self.n = n
        self.zero_based = zero_based
        self.edges = edges
        self.directed = directed
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
            if weight is not None:
                temp = [to_v, weight]
            else:
                temp = to_v
            adj_list[from_v].append(temp)
            if not directed:
                if weight is not None:
                    temp = [from_v, weight]
                else:
                    temp = from_v
                adj_list[to_v].append(temp)
        return adj_list

    def _get_n_and_start(self):
        n = self.n if self.zero_based else self.n + 1
        start = 0 if self.zero_based else 1
        return n, start

    def dfs(self):
        n, start = self._get_n_and_start()
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
        n, start = self._get_n_and_start()
        result = []
        visited = [False] * n
        for vertex in range(start, n):
            if not visited[vertex]:
                visited[vertex] = True
                self._bfs(vertex, visited, result)
        return result

    def _bfs(self, start, visited, result):
        queue = deque()
        queue.append(start)
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for adj_vertex in self.adj_list[vertex]:
                if not visited[adj_vertex]:
                    queue.append(adj_vertex)
                    visited[adj_vertex] = True
        return result

    def is_cycle_present(self):
        if self.directed:
            return self._is_cycle_in_directed()
        else:
            return self._is_cycle_in_undirected()

    def _is_cycle_in_undirected(self):
        # carry parent
        n, start = self._get_n_and_start()
        visited = [False] * n

        def helper(node, parent):
            visited[node] = True
            for adj_vertex in self.adj_list[node]:
                if not visited[adj_vertex]:
                    if helper(adj_vertex, node):
                        return True
                elif adj_vertex != parent:
                    return True

        for vertex in range(start, n):
            if not visited[vertex]:
                if helper(vertex, None):
                    return True
        return False

    def _is_cycle_in_directed(self):
        # create dfs visited and visited
        n, start = self._get_n_and_start()
        visited = [False] * n
        dfs_visited = [False] * n

        def helper(node):
            visited[node] = True
            dfs_visited[node] = True
            for adj_vertex in self.adj_list[node]:
                if not visited[adj_vertex]:
                    if helper(adj_vertex):
                        return True
                elif dfs_visited[adj_vertex]:
                    return True
            pass
            dfs_visited[node] = False

        for vertex in range(start, n):
            if not visited[vertex]:
                if helper(vertex):
                    return True
        return False

    def is_bipartite(self):
        # each adjacent node does not have same color. Even cycle graph is bipartite
        # carry parent color and if visited and color same not bipartite
        return self._is_bipartite_dfs()

    def _is_bipartite_bfs(self):
        n, start = self._get_n_and_start()
        visited = [-1] * n

        def bfs(queue):
            while queue:
                current, color = queue.popleft()
                for adj_vertex in self.adj_list[current]:
                    if visited[adj_vertex] == -1:
                        visited[adj_vertex] = 1 - color
                        queue.append((adj_vertex, 1 - color))
                    elif color == visited[adj_vertex]:
                        return False
            return True
        for vertex in range(start, n):
            if visited[vertex] == -1:
                bfs_queue = deque()
                bfs_queue.append((vertex, 0))
                visited[vertex] = 0
                if not bfs(bfs_queue):
                    return False
        return True

    def _is_bipartite_dfs(self):
        n, start = self._get_n_and_start()
        visited = [-1] * n

        def dfs(node, color):
            visited[node] = color
            for adj_vertex in self.adj_list[node]:
                if visited[adj_vertex] == -1:
                    if not dfs(adj_vertex, 1 - color):
                        return False
                elif visited[adj_vertex] == color:
                    return False
            return True

        for vertex in range(start, n):
            if visited[vertex] == - 1:
                if not dfs(vertex, 0):
                    return False
        return True

    def topo_sort(self):
        # 0 incoming edges first
        # linear ordering of N vertices u -> v, u should be before you
        # topo sort not possible with cycle
        # only possible for DAG
        return self._topo_sort_bfs()

    def _topo_sort_dfs(self):
        # once dfs is over for node, it goes into stack
        n, start = self._get_n_and_start()
        visited = [False] * n
        stack = []

        def dfs(node):
            visited[node] = True
            for adj_v in self.adj_list[node]:
                if not visited[adj_v]:
                    dfs(adj_v)
            stack.append(node)

        for vertex in range(start, n):
            if not visited[vertex]:
                dfs(vertex)
        stack.reverse()
        return stack

    def _topo_sort_bfs(self):
        # kahn's algo
        # create in_degree matrix
        in_degree = self._get_in_degree()
        queue = deque()
        for vertex, v_in_degree in enumerate(in_degree):
            if v_in_degree == 0:
                queue.append(vertex)
        result = []
        while queue:
            vertex = queue.popleft()
            self._update_in_degree(vertex, in_degree, queue)
            result.append(vertex)
        return result

    def _update_in_degree(self, vertex, in_degree, queue):
        for adj_vertex in self.adj_list[vertex]:
            in_degree[adj_vertex] -= 1
            if in_degree[adj_vertex] == 0:
                queue.append(adj_vertex)

    def _get_in_degree(self):
        n, start = self._get_n_and_start()
        in_degree = [0] * n
        for _, to_vs in enumerate(self.adj_list):
            for vertex in to_vs:
                in_degree[vertex] += 1
        return in_degree

    def find_shortest_distance_bfs_1or0(self):
        # deque - 0 distance push from left, 1 distance push from right
        n, start = self._get_n_and_start()
        distance = [float('inf')] * n
        distance[start] = 0
        queue = deque()
        queue.append(start)

        while queue:
            vertex = queue.popleft()
            for adj_vertex, weight in self.adj_list[vertex]:
                new_weight = distance[vertex] + weight
                if distance[adj_vertex] > new_weight:
                    distance[adj_vertex] = new_weight
                    if weight == 0:
                        queue.appendleft(adj_vertex)
                    else:
                        queue.append(adj_vertex)
        return distance

    def find_shortest_distance_different_weights(self):
        # dijkstra algo. push weight in priority queue and pop
        # does not work for negative cycle
        n, start = self._get_n_and_start()
        distance = [float('inf')] * n
        distance[start] = 0
        heap = []
        heappush(heap, (0, start))
        while heap:
            dist, vertex = heappop(heap)
            for adj_vertex, adj_distance in self.adj_list[vertex]:
                new_dist = dist + adj_distance
                if new_dist < distance[adj_vertex]:
                    distance[adj_vertex] = new_dist
                    heappush(heap, (new_dist, adj_vertex))
        return distance

    def find_shortest_distance_path(self, source, final_destination):
        # dijkstra algo. push weight in priority queue and pop
        # parent array - who updated distance is what you need to know
        n, start = self._get_n_and_start()
        distance = [float('inf')] * n
        parent = [-1] * n
        distance[source] = 0
        parent[source] = source
        heap = []
        heappush(heap, (0, start))
        while heap:
            dist, vertex = heappop(heap)
            for adj_vertex, adj_distance in self.adj_list[vertex]:
                new_dist = dist + adj_distance
                if new_dist < distance[adj_vertex]:
                    parent[adj_vertex] = vertex
                    distance[adj_vertex] = new_dist
                    heappush(heap, (new_dist, adj_vertex))
        result = []
        while source != final_destination:
            result.append(final_destination)
            final_destination = parent[final_destination]
        result.append(source)
        result.reverse()
        return result

