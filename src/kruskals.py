import random
import sys
import pygame
from disjointset import DisjointSet

#pylint: disable=no-member

class Kruskals:
    """This class controls the Kruskal's algorithm that generates the second maze.

    Attributes:
        maze: Maze class instance. The default value is of the Maze class.
    """

    def __init__(self, maze):
        """The constructor for this class. 
        Sets up all needed variables and data structures."""

        self.maze = maze

        self.cell_size = 40/(self.maze.grid_size/5)

        self.coordinates = []
        self.cells = []

        self.walls_down = 0
        self.djs = DisjointSet(self.maze.grid_size*self.maze.grid_size)

    def initialize_coordinates(self):
        """This method initializes coordinates by adding all existing 
        cell coordinates to a list."""
        x = self.maze.x_2
        y = self.maze.y
        for i in range(self.maze.grid_size):
            for j in range(1, self.maze.grid_size+1):
                self.coordinates.append((x+(i*self.cell_size), y+(j*self.cell_size)))

    def initialize_cells(self):
        """This method initializes cells by adding the position of each cell
        to a list as a tuple."""
        for i in range(self.maze.grid_size):
            for j in range(self.maze.grid_size):
                self.cells.append((i, j))

    def initialize_sets(self):
        """This method initializes disjoint sets for each cell."""
        i = len(self.coordinates)
        while i > 0:
            self.djs.make_set()
            i -= 1

    def initialize_adjacency_list(self):
        """This method initializes adjacency list, which illustrates the edges between the nodes."""
        adjacency_list = {}
        return adjacency_list

    def add_edge(self, adjacency_list, i, j):
        if i not in adjacency_list:
            adjacency_list[i] = []
        if j not in adjacency_list:
            adjacency_list[j] = []
        adjacency_list[i].append(j)
        adjacency_list[j].append(i)

    def convert(self, cell):
        """This method converts cell into either its ordinal number or corresponding coordinates.
        Args:
            cell: Tuple that has the position of the cell.
        """
        ordinal = cell[0]*self.maze.grid_size+cell[1]
        coordinates = self.coordinates[ordinal]
        return (ordinal,coordinates)

    def find_neighbors(self, current_cell):
        """This method returns a random suitable neighbor of the current cell.
        Suitable meaning that there is a wall between current cell and its neighbor.
        Args:
            current_cell: Tuple that holds the position of current cell.
        """
        neighbors = []

        current = self.convert(current_cell)[0]
        right = (current_cell[0]+1,current_cell[1])
        left = (current_cell[0]-1,current_cell[1])
        down= (current_cell[0],current_cell[1]+1)
        up = (current_cell[0],current_cell[1]-1)

        if right in self.cells and self.djs.find(current) != self.djs.find(self.convert(right)[0]):
            neighbors.append(right)
        if left in self.cells and self.djs.find(current) != self.djs.find(self.convert(left)[0]):
            neighbors.append(left)
        if down in self.cells and self.djs.find(current) != self.djs.find(self.convert(down)[0]):
            neighbors.append(down)
        if up in self.cells and self.djs.find(current) != self.djs.find(self.convert(up)[0]):
            neighbors.append(up)

        if neighbors:
            return random.choice(neighbors)
        return None

    def generate(self, adjacency_list, test_mode):
        """This method manages the main functionality of Kruskal's algorithm."""
        while self.walls_down < len(self.cells)-1:
            if not test_mode:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
            chosen_cell = random.choice(self.cells)
            chosen_neighbor = self.find_neighbors(chosen_cell)
            if chosen_neighbor:
                current_index = self.convert(chosen_cell)[0]
                neighbor_index = self.convert(chosen_neighbor)[0]
                representative_1 = self.djs.find(current_index)
                representative_2 = self.djs.find(neighbor_index)
                if representative_1 != representative_2:
                    self.djs.union(representative_1, representative_2)
                    self.knock_down(chosen_cell, chosen_neighbor)
                    self.add_edge(adjacency_list, chosen_cell, chosen_neighbor)
                    self.walls_down += 1

    def knock_down(self, current, neighbor):
        """This method knocks down a wall between current cell and its chosen neighbor.
        Args:
            current: Tuple that holds the position of current cell.
            neighbor: Tuple that holds the position of neighbor cell.
        """
        current_coordinates = self.convert(current)[1]
        neighbor_coordinates = self.convert(neighbor)[1]

        if neighbor_coordinates[0] > current_coordinates[0]:
            self.maze.right(current_coordinates[0], current_coordinates[1])

        elif neighbor_coordinates[0] < current_coordinates[0]:
            self.maze.left(current_coordinates[0], current_coordinates[1])

        elif neighbor_coordinates[1] > current_coordinates[1]:
            self.maze.down(current_coordinates[0], current_coordinates[1])

        else:
            self.maze.up(current_coordinates[0], current_coordinates[1])


#The source that was used to implement this dfs algorithm:
#https://courses.cs.washington.edu/courses/cse326/07su/prj2/kruskal.html
