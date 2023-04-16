import unittest
from kruskals import Kruskals

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

class TestKruskals(unittest.TestCase):
    def setUp(self):
        self.maze = StubMaze(GRID_SIZE)
        self.kruskals = Kruskals(self.maze)
        self.kruskals.initialize_coordinates()
        self.kruskals.initialize_cells()
        self.kruskals.initialize_sets()


    def test_initializes_correct_amount_of_coordinates(self):
        answer = GRID_SIZE*GRID_SIZE

        self.assertEqual(len(self.kruskals.coordinates), answer)


    def test_initializes_correct_amount_of_cells(self):
        answer = GRID_SIZE*GRID_SIZE

        self.assertEqual(len(self.kruskals.cells), answer) 


    def test_chooses_existing_cell(self):
        chosen_cell = self.kruskals.choose_cell()

        self.assertIn(chosen_cell,self.kruskals.cells)


    def test_convertions_work(self):
        chosen_cell = self.kruskals.choose_cell()
        coordinates = self.kruskals.convert_to_coordinates(chosen_cell)
        new_cell = self.kruskals.convert_to_cell(coordinates)

        self.assertEqual(chosen_cell, new_cell) 


    def test_finds_all_neighbors(self):
        x = self.maze.x_axis_2+2*self.maze.cell_size
        y = self.maze.y_axis+2*self.maze.cell_size

        answer = []
        answer.append("right")
        answer.append("left")
        answer.append("down")
        answer.append("up")
        self.kruskals.find_neighbors(x, y)

        self.assertEqual(self.kruskals.neighbors, answer)


    def test_finds_two_neighbors(self):
        x = self.maze.x_axis_2+4*self.maze.cell_size
        y = self.maze.y_axis+5*self.maze.cell_size

        answer = []
        answer.append("left")
        answer.append("up")
        self.kruskals.find_neighbors(x, y)

        self.assertEqual(self.kruskals.neighbors, answer)


    def test_chooses_some_neighbor(self):
        x = self.maze.x_axis_2+self.maze.cell_size
        y = self.maze.y_axis+self.maze.cell_size

        self.kruskals.neighbors.append("right")

        chosen_cell = self.kruskals.choose_neighbor(x,y)
        new_cell = self.kruskals.convert_to_cell((x + self.maze.cell_size, y))

        self.assertEqual(chosen_cell, new_cell) 
