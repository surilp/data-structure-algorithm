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
