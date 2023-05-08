from dfs import DepthFirstSearch
from kruskals import Kruskals


class Call:
    """This class invokes the algorithms.

    Attributes:
        maze: Maze class instance. The default value is of the Maze class.
    """

    def __init__(self, maze):
        """The constructor for this class."""
        self.maze = maze
        self.kruskal = Kruskals(self.maze)
        self.dfs = DepthFirstSearch(self.maze)

    def kruskals(self):
        """This method invokes the Kruskal's algorithm."""
        self.kruskal.initialize_coordinates()
        self.kruskal.initialize_cells()
        self.kruskal.initialize_sets()
        self.kruskal.generate()

    def depth_first_search(self):
        """This method invokes the DFS algorithm."""
        self.dfs.initialize_coordinates()
        visited = self.dfs.initialize_visited()
        adjacency_list = self.dfs.initialize_adjacency_list()
        self.dfs.generate(visited, adjacency_list, False)
