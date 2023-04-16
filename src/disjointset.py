
class DisjointSet():
    """This class makes the data structure that is needed for Kruskal's algorithm.
    Disjoint-set data structures plays a key role in Kruskal's algorithm for finding 
    the minimum spanning tree of a graph.
    """

    def __init__(self, n_items):
        """The constructor for this class. 
        Sets up necessary variables and calls make_set() method."""
        self.n_items = n_items
        self.rank = [1]*self.n_items
        self.parent = {}

        self.make_set()

    def make_set(self):
        """This method creates disjoint sets from each item in given set"""
        for i in range(self.n_items):
            self.parent[i] = i

    def find(self, i):
        """This method finds representative of a disjoint set."""
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, set1, set2):
        """This method merges sets to a single disjoint set."""
        root_x = self.find(set1)
        root_y = self.find(set2)

        self.parent[root_x] = root_y


#The source that was used to create this implementation of disjoint-set data structure:
    # https://www.geeksforgeeks.org/disjoint-set-data-structures/
    # Where code is contributed by ng24_7.
