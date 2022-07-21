from unittest import TestCase
from graph.disjoint_set import DSU

class TestDisjointSet(TestCase):

    def test_find_parent(self):
        dsu = DSU(5)
        parent = dsu.find_parent(4)
        self.assertEqual(4, parent)

    def test_find_union(self):
        dsu = DSU(5)
        dsu.union(3, 4)
        dsu.union(2, 3)
        dsu.union(1, 2)
        parent = dsu.find_parent(1)
        self.assertEqual(3, parent)