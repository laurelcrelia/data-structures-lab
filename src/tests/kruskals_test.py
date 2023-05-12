import unittest
from kruskals import Kruskals
import random

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

def dfs(start, adjacency_list):
    visited = set()
    stack = [start]
    while stack:
        current = stack.pop()
        visited.add(current)
        for neighbor in adjacency_list[current]:
            if neighbor not in visited:
                stack.append(neighbor)
    return visited

class TestKruskals(unittest.TestCase):
    def setUp(self):
        self.maze = StubMaze(GRID_SIZE)
        self.kruskals = Kruskals(self.maze)
        self.kruskals.initialize_coordinates()
        self.kruskals.initialize_cells()
        self.kruskals.initialize_sets()
        self.adjacency_list = self.kruskals.initialize_adjacency_list()

    def test_convertions_work(self):
        chosen_cell = random.choice(self.kruskals.cells)
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

    def test_connectivity(self):
        """We can test the connectivity of the maze with depth-first search.
        We start from a random cell in the maze and use adjacency list to navigate
        through the connected paths. Lastly we check that the amount of visited is the same as the
        amount of all cells.
        """
        self.kruskals.generate(self.adjacency_list, True)
        start = random.choice(list(self.kruskals.cells))
        visited = dfs(start, self.adjacency_list)

        self.assertEqual(len(visited), len(self.kruskals.cells))

    def test_no_cycles(self):
        """If x is the amount of nodes, in undirected graph there needs to be exactly x-1 amount of edges,
        for there to be no cycle.
        """
        self.kruskals.generate(self.adjacency_list, True)

        answer = self.maze.grid_size*self.maze.grid_size-1

        count = 0
        for keys in self.adjacency_list:
            for value in self.adjacency_list[keys]:
                count += 1

        self.assertEqual(count//2, answer)

    def test_unique_solution(self):
        """We can also use dfs to test if there is only one solution path in the maze.
        This can be checked with depth-first search from both ends of the maze 
        and then comparing their visited lists after search is complete. If visited
        lists are the same, there is only one solution path.
        """
        self.kruskals.generate(self.adjacency_list, True)
        start = 0
        end = self.maze.grid_size-1
        visited_start = dfs(start, self.adjacency_list)
        visited_end = dfs(end, self.adjacency_list)

        self.assertEqual(visited_start, visited_end)
