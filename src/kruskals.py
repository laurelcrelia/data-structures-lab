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
        self.neighbors = []
        self.direction = []

        self.walls_down = 0
        self.disjointset = DisjointSet(self.maze.grid_size*self.maze.grid_size)

    def initialize_coordinates(self):
        """This method initializes coordinates by adding all existing 
        cell coordinates to a list.
        """
        x_axis = self.maze.x_axis_2
        y_axis = self.maze.y_axis
        for i in range(self.maze.grid_size):
            for j in range(1, self.maze.grid_size+1):
                self.coordinates.append((x_axis+(i*self.cell_size), y_axis+(j*self.cell_size)))

    def initialize_cells(self):
        """This method initializes cells by adding cell indexes to a list.
        Cell indexes are needed when working with DisjointSet class.
        """
        for i in range(len(self.coordinates)):
            self.cells.append(i)

    def initialize_sets(self):
        """This method initializes disjoint sets for each cell."""
        i = len(self.coordinates)
        while i > 0:
            self.disjointset.make_set()
            i -= 1

    def initialize_adjacency_list(self):
        """This method initializes adjacency list, which illustrates the edges between the nodes."""
        adjacency_list = {}
        return adjacency_list

    def add_edge(self, adjacency_list, x, y):
        if x not in adjacency_list:
            adjacency_list[x] = []
        if y not in adjacency_list:
            adjacency_list[y] = []
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)

    def convert_to_coordinates(self, cell):
        """This method converts cell indexes into their corresponding cell coordinates.
        Args:
            cell: Integer that is the index of the cell that is to be converted.
        """
        coordinates = self.coordinates[cell]
        return coordinates

    def convert_to_cell(self, coordinates):
        """This method converts cell coordinates into their corresponding cell indexes.
        Args:
            coordinates: Tuple that contains the coordinates of the cell 
            that is to be converted.
        """
        cell = self.coordinates.index(coordinates)
        return cell

    def find_neighbors(self, x_axis, y_axis):
        """This method picks all the suitable neighbors of the current cell.
        Suitable meaning that there is a wall between current cell and its neighbor.
        Args:
            x_axis: Variable that determines the x coordinate of the current cell.
            y_axis: Variable that determines the y coordinate of the current cell.
        """
        self.neighbors.clear()

        current_cell = self.convert_to_cell((x_axis, y_axis))

        if self.suitable_neighbor(current_cell, (x_axis + self.cell_size, y_axis)):
            self.neighbors.append("right")
        if self.suitable_neighbor(current_cell, (x_axis - self.cell_size, y_axis)):
            self.neighbors.append("left")
        if self.suitable_neighbor(current_cell, (x_axis , y_axis + self.cell_size)):
            self.neighbors.append("down")
        if self.suitable_neighbor(current_cell, (x_axis, y_axis - self.cell_size)):
            self.neighbors.append("up")

    def suitable_neighbor(self, current_cell, neighbor_coordinates):
        """This method checks whether given neighbor coordinates are
        within grid and whether current cell and neighbor cell have a wall between them.
        Args:
            current_cell: Tuple that contains the coordinates of given current cell.
            neighbor_coordinates: Tuple that contains the coordinates of given neighbor cell.
        """
        if neighbor_coordinates in self.coordinates:
            neighbor_cell = self.convert_to_cell(neighbor_coordinates)
            if self.check_if_wall(current_cell, neighbor_cell):
                return True
        return False

    def choose_neighbor(self, x_axis, y_axis):
        """If given current cell has suitable neighbors, 
        this method randomly chooses one of them and returns its cell index.
        Args:
            x_axis: Variable that determines the x coordinate of the current cell.
            y_axis: Variable that determines the y coordinate of the current cell.
        """
        if len(self.neighbors) > 0:
            chosen_neighbor = random.choice(self.neighbors)

            self.direction.append(chosen_neighbor)

            new_x = x_axis
            new_y = y_axis

            if chosen_neighbor == "right":
                new_x = x_axis + self.cell_size

            elif chosen_neighbor == "left":
                new_x = x_axis - self.cell_size

            elif chosen_neighbor == "down":
                new_y = y_axis + self.cell_size

            elif chosen_neighbor == "up":
                new_y = y_axis - self.cell_size

            neighbor_coordinates = (new_x, new_y)
            neighbor_cell = self.convert_to_cell(neighbor_coordinates)
            return neighbor_cell
        return None

    def generate(self, adj_list, test_mode):
        """This method manages the main functionality of Kruskal's algorithm."""
        while self.walls_down < len(self.cells)-1:
            if not test_mode:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
            chosen_cell = random.choice(self.cells)
            chosen_coordinates = self.convert_to_coordinates(chosen_cell)
            self.find_neighbors(chosen_coordinates[0], chosen_coordinates[1])
            chosen_neighbor = self.choose_neighbor(chosen_coordinates[0], chosen_coordinates[1])
            if chosen_neighbor:
                representative_1 = self.disjointset.find(chosen_cell)
                representative_2 = self.disjointset.find(chosen_neighbor)
                if self.check_if_wall(chosen_cell, chosen_neighbor):
                    self.disjointset.union(representative_1, representative_2)
                    self.knock_down(chosen_coordinates[0], chosen_coordinates[1])
                    self.add_edge(adj_list, chosen_cell, chosen_neighbor)
                    self.walls_down += 1

    def check_if_wall(self, current, neighbor):
        """This method checks whether there is a wall between current cell and neighbor cell.
        The method calls find() from DisjointSet class which finds representatives of a cell.
        Args:
            current: Index of a current cell in the shape of an integer.
            neighbor: Index of a neighbor cell in the shape of an integer.
        """
        representative_1 = self.disjointset.find(current)
        representative_2 = self.disjointset.find(neighbor)
        if representative_1 != representative_2:
            return True
        return False

    def knock_down(self, x_axis, y_axis):
        """This method knocks down a wall between current cell and its chosen neighbor.
        Args:
            x_axis: Variable that determines the x coordinate of the current cell.
            y_axis: Variable that determines the y coordinate of the current cell.
        """
        if self.direction[-1] == "right":
            self.maze.right(x_axis, y_axis)
            self.direction.clear()

        elif self.direction[-1] == "left":
            self.maze.left(x_axis, y_axis)
            self.direction.clear()

        elif self.direction[-1] == "down":
            self.maze.down(x_axis, y_axis)
            self.direction.clear()

        elif self.direction[-1] == "up":
            self.maze.up(x_axis, y_axis)
            self.direction.clear()


#The source that was used to implement this dfs algorithm:
#https://courses.cs.washington.edu/courses/cse326/07su/prj2/kruskal.html
