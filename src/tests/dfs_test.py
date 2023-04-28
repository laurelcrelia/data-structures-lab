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

    def test_every_cell_is_visited(self):
        visited = self.dfs.initialize_visited()
        self.dfs.generate(visited, True)

        answer = ([[True for i in range(self.maze.grid_size)]for j in range(self.maze.grid_size)])
        
        self.assertEqual(visited, answer)

