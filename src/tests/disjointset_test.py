import unittest
from disjointset import DisjointSet


class TestDepthFirstSearch(unittest.TestCase):
    def setUp(self):
        self.n = 5
        self.disjointset = DisjointSet(self.n)

    def test_makes_correct_set(self):
        set = {}
        for i in range(self.n):
            set[i] = i

        self.assertEqual(self.disjointset.parent, set)

    def test_finds_correct_representative(self):
        self.disjointset.union(0, 2)
        self.disjointset.union(4, 2)
        self.disjointset.union(3, 1)

        representative = self.disjointset.find(4)

        self.assertEqual(representative,2)

    def test_makes_correct_union(self):
        self.disjointset.union(0, 2)
        self.disjointset.union(4, 2)
        self.disjointset.union(3, 1)

        after_unions = ([self.disjointset.find(i) for i in range(self.n)])

        correct_set = [2,1,2,1,2]

        self.assertEqual(after_unions, correct_set)

