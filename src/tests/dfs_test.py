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

class TestDepthFirstSearch(unittest.TestCase):
    def setUp(self):
        self.maze = StubMaze(GRID_SIZE)
        self.dfs = DepthFirstSearch(self.maze)

    def test_initializes_correct_amount_of_cells(self):
        self.dfs.initialize_cells()
        answer = GRID_SIZE*GRID_SIZE

        self.assertEqual(len(self.dfs.cells), answer)

    # def test_every_cell_is_visited(self):
    #     pass

    # def test_no_cycles(self):
    #     pass

    # def test_only_one_solution_path(self):
    #     pass

    # def test_edges_are_sealed(self):
    #     pass
