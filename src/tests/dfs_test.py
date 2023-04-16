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
        self.dfs.initialize_cells()

    def test_initializes_correct_amount_of_cells(self):
        answer = GRID_SIZE*GRID_SIZE

        self.assertEqual(len(self.dfs.cells), answer)

    def test_chooses_existing_cell(self):
        chosen_cell = self.dfs.choose_cell()

        self.assertIn(chosen_cell,self.dfs.cells)

    def test_finds_correct_neighbors(self):
        x = self.maze.x_axis_1+2*self.maze.cell_size
        y = self.maze.y_axis+2*self.maze.cell_size

        right_neighbor = (x + self.maze.cell_size, y)
        left_neighbor = (x - self.maze.cell_size, y)
        lower_neighbor = (x , y + self.maze.cell_size)
        upper_neighbor = (x, y- self.maze.cell_size)

        self.dfs.visited.append(right_neighbor)
        self.dfs.visited.append(left_neighbor)
        self.dfs.visited.append(lower_neighbor)
        self.dfs.visited.append(upper_neighbor)

        self.dfs.find_neighbors(x, y)
        self.assertEqual(self.dfs.neighbors, [])

        self.dfs.visited.clear()

        self.dfs.find_neighbors(x, y)
        self.assertEqual(self.dfs.neighbors[0], "right")


    def test_every_cell_is_visited(self):
        for cell in self.dfs.cells:
            x = cell[0]
            y = cell[1]
            self.dfs.visit_cell(x,y)
            self.dfs.visited.sort()

        self.assertEqual(self.dfs.visited, self.dfs.cells)

    # def test_no_cycles(self):
    #     pass

    # def test_only_one_solution_path(self):
    #     pass

    # def test_edges_are_sealed(self):
    #     pass
