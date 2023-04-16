from dfs import DepthFirstSearch

#pylint: disable=no-member

class Call:
    """This class invokes the algorithms.

    Attributes:
        maze: Maze class instance. The default value is of the Maze class.
    """

    def __init__(self, maze):
        """The constructor for this class."""
        self.maze = maze
        self.dfs = DepthFirstSearch(self.maze)

    # def kruskals(self):
    #     """This method invokes the Kruskal's algorithm."""

    def depth_first_search(self):
        """This method invokes the DFS algorithm."""
        self.dfs.initialize_cells()
        chosen_cell = self.dfs.choose_cell()
        self.dfs.recursion(chosen_cell[0], chosen_cell[1])
