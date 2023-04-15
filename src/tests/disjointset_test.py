import unittest
from disjointset import DisjointSet


class TestDepthFirstSearch(unittest.TestCase):
    def setUp(self):
        self.n = 5
        self.disjointset = DisjointSet(self.n)

    def test_makes_correct_set(self):
        set = {}
        for i in range(1, 6):
            set[i] = i

        self.assertEqual(self.disjointset.parent, set)

    def test_finds_correct_representative(self):
        self.disjointset.union(1, 3)
        self.disjointset.union(5, 3)
        self.disjointset.union(4, 2)

        representative = self.disjointset.find(5)

        self.assertEqual(representative,3)

    def test_makes_correct_union(self):
        self.disjointset.union(1, 3)
        self.disjointset.union(5, 3)
        self.disjointset.union(4, 2)

        after_unions = ([self.disjointset.find(i) for i in range(1, self.n+1)])

        correct_set = [3,2,3,2,3]

        self.assertEqual(after_unions, correct_set)

