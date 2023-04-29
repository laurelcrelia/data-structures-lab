import unittest
from dfs import DepthFirstSearch

GRID_SIZE = 5
WIDTH = 640
HEIGHT = 440

class StubMaze:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.cell_size = 40/(self.grid_size/5)
        self.screen_unit = 40

        self.x_axis_1 = int(2*self.screen_unit)
        self.x_axis_2 = int(640-((self.grid_size*self.cell_size)+2*self.screen_unit)) 
        self.y_axis = (3+((self.grid_size/5)*0.25))*self.screen_unit

        self.grid_1 = []
        self.grid_2 = []

    def up(self, x, y):
        pass

    def down(self, x, y):
        pass

    def left(self, x, y):
        pass

    def right(self, x, y):
        pass

    def current_cell(self, x, y):
        pass

    def backtracking_cell(self, x, y):
        pass

class TestDepthFirstSearch(unittest.TestCase):
    def setUp(self):
        self.maze = StubMaze(GRID_SIZE)
        self.dfs = DepthFirstSearch(self.maze)
        self.dfs.initialize_coordinates()
        self.visited = self.dfs.initialize_visited()
        self.adjacency_list = self.dfs.initialize_adjacency_list()

    def test_every_cell_is_visited(self):
        self.dfs.generate(self.visited, self.adjacency_list, True)

        answer = ([[True for i in range(self.maze.grid_size)]for j in range(self.maze.grid_size)])
        
        self.assertEqual(self.visited, answer)

    def test_no_cycles(self):
        # If x is the amount of nodes, in undirected graph there needs to be exactly x-1 amount of edges, 
        # for there to be no cycle.
        self.dfs.generate(self.visited, self.adjacency_list, True)

        answer = self.maze.grid_size*self.maze.grid_size-1

        count = 0
        for keys in self.adjacency_list:
            for value in self.adjacency_list[keys]:
                count += 1

        self.assertEqual(count//2, answer)


