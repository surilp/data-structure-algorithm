from unittest import TestCase
from graph.Graph import Graph


class GraphTest(TestCase):

    def test_dfs(self):
        n = 10
        edges = [(1, 2), (2, 3), (3, 8), (8, 9), (9, 10), (3, 4), (4, 5), (5, 6), (6, 7), (4, 7)]
        graph = Graph(n, edges)
        result = graph.dfs()
        self.assertEqual(result, [1, 2, 3, 8, 9, 10, 4, 5, 6, 7])

    def test_bfs(self):
        n = 10
        edges = [(1, 2), (2, 3), (3, 8), (8, 9), (9, 10), (3, 4), (4, 5), (5, 6), (6, 7), (4, 7)]
        graph = Graph(n, edges)
        result = graph.bfs()
        self.assertEqual(result, [1, 2, 3, 8, 4, 9, 5, 7, 10, 6])

    def test_undirected_graph_cycle_false(self):
        n = 5
        edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
        graph = Graph(n, edges)
        result = graph.is_cycle_present()
        self.assertEqual(result, False)

    def test_undirected_graph_cycle_true(self):
        n = 5
        edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
        graph = Graph(n, edges)
        result = graph.is_cycle_present()
        self.assertEqual(result, True)

    def test_directed_graph_cycle_true(self):
        n = 11
        edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (3, 8), (8, 6), (9, 2), (9, 10), (10, 11), (11, 9)]
        graph = Graph(n, edges, directed=True)
        result = graph.is_cycle_present()
        self.assertEqual(result, True)

    def test_directed_graph_cycle_false(self):
        n = 11
        edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (3, 8), (8, 6), (9, 2), (10, 9), (10, 11), (11, 9)]
        graph = Graph(n, edges, directed=True)
        result = graph.is_cycle_present()
        self.assertEqual(result, False)

    def test_is_bipartite_true(self):
        n = 8
        edges = [(1, 2), (2, 3), (3, 6), (3, 4), (6, 5), (4, 5), (4, 7), (7, 8)]
        graph = Graph(n, edges)
        result = graph.is_bipartite()
        self.assertEqual(result, True)

    def test_is_bipartite_false(self):
        n = 8
        edges = [(1, 2), (2, 3), (3, 6), (3, 4), (6, 4), (4, 7), (7, 8)]
        graph = Graph(n, edges)
        result = graph.is_bipartite()
        self.assertEqual(result, False)

    def test_topo_sort(self):
        n = 6
        edges = [(1, 2), (2, 3), (5, 3), (4, 5), (4, 0)]
        graph = Graph(n, edges, directed=True, zero_based=True)
        result = graph.topo_sort()
        self.assertEqual([1, 4, 2, 5, 0, 3], result)

    def test_shortest_distance_bfs_1_0(self):
        n = 6
        edges = [(1, 2, 1), (1, 4, 0), (2, 3, 1), (4, 3, 0), (3, 5, 0), (3, 6, 0)]
        graph = Graph(n, edges)
        result = graph.find_shortest_distance_bfs_1or0()
        self.assertEqual([float('inf'), 0, 1, 0, 0, 0, 0], result)

    def test_shortest_distance_bfs_1_0_2(self):
        n = 6
        edges = [(1, 2, 0), (1, 3, 1), (2, 3, 0), (2, 4, 1), (3, 5, 1), (4, 5, 1), (4, 6, 0), (5, 6, 0)]
        graph = Graph(n, edges)
        result = graph.find_shortest_distance_bfs_1or0()
        self.assertEqual([float('inf'), 0, 0, 0, 1, 1, 1], result)

    def test_shorted_distance_different_weight(self):
        n = 4
        edges = [(1, 2, 6), (1, 3, 1), (2, 4, 1), (3, 4, 2)]
        graph = Graph(n, edges)
        result = graph.find_shortest_distance_different_weights()
        self.assertEqual([float('inf'), 0, 4, 1, 3], result)

    def test_shortest_distance_path(self):
        n = 5
        edges = [(1, 2, 2), (1, 4, 1), (4, 3, 3), (2, 3, 4), (2, 5, 5), (3, 5, 1)]
        graph = Graph(n, edges)
        result = graph.find_shortest_distance_path(1, 5)
        self.assertEqual([1, 4, 3, 5], result)
