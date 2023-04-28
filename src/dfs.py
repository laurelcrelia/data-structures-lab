import random
import sys
import pygame

#pylint: disable=no-member

class DepthFirstSearch:
    """This class controls the Depth-first search algorithm that generates the first maze.

    Attributes:
        maze: Maze class instance. The default value is of the Maze class.
    """

    def __init__(self, maze):
        """The constructor for this class.
        Sets up needed variables."""

        self.maze = maze

        self.x = self.maze.x_axis_1
        self.y = self.maze.y_axis
        self.cell_size = 40/(self.maze.grid_size/5)

        self.coordinates = []

    def initialize_coordinates(self):
        """This method initializes coordinates of all existing cells."""
        for i in range(self.maze.grid_size):
            for j in range(1, self.maze.grid_size+1):
                self.coordinates.append((self.x+(i*self.cell_size), self.y+(j*self.cell_size)))

    def initialize_visited(self):
        """This method initializes two-dimensional boolean table, which
        keeps track of visited cells."""
        visited = ([[False for i in range(self.maze.grid_size)]for j in range(self.maze.grid_size)])
        return visited

    def find_neighbors(self, current, visited):
        """This method picks the neighbors of the current cell
        that have all their walls up i.e. are unvisited and adds them to
        neighbors -list.
        Args:
            current: Tuple that has the position of current cell.
            visited: Two-dimensional table of boolean values, which keeps a record of
            the cells that are visited.
        """
        neighbors = []

        x = current[0]
        y = current[1]

        if x+1 <= self.maze.grid_size-1 and not visited[x + 1][y]:
            neighbors.append((x + 1,y))
        if x-1 >= 0 and not visited[x - 1][y]:
            neighbors.append((x - 1,y))
        if y+1 <= self.maze.grid_size-1 and not visited[x][y + 1]:
            neighbors.append((x,y + 1))
        if y-1 >= 0 and not visited[x][y - 1]:
            neighbors.append((x,y - 1))

        if neighbors:
            return random.choice(neighbors)
        return None

    def generate(self, visited, test_mode):
        """This method initializes stack, chooses a starting cell
        and calls the dfs method.
        
        Args:
            visited: Two-dimensional table of boolean values, which keeps a record of
            the cells that are visited.
            test_mode: Boolean value which determines whether testing is taking place.
        """
        start = (0,0)
        stack = []
        self.dfs(start, stack, visited, test_mode)

    def dfs(self, current, stack, visited, test_mode):
        """This is the recursive function of DFS.

        Args:
            current: Tuple that has the position of current cell.
            stack: Variable that determines y coordinate of the current cell.
            visited: Two-dimensional table of boolean values, which keeps a record of
            the cells that are visited.
            test_mode: Boolean value which determines whether testing is taking place.
        """
        if not test_mode:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        x, y = current[0], current[1]

        chosen_neighbor = self.find_neighbors(current, visited)
        current_coordinates = self.convert_to_coordinates(current)

        if chosen_neighbor:
            neighbor_coordinates = self.convert_to_coordinates(chosen_neighbor)

            visited[current[0]][current[1]] = True
            stack.append((x, y))

            self.maze_directions(current_coordinates, neighbor_coordinates)

            visited[chosen_neighbor[0]][chosen_neighbor[1]] = True
            self.dfs((chosen_neighbor[0],chosen_neighbor[1]), stack, visited, test_mode)

        else:
            if len(stack) > 0:
                x, y = stack.pop()
                self.maze.current_cell(current_coordinates[0], current_coordinates[1])
                self.maze.backtracking_cell(current_coordinates[0], current_coordinates[1])
                self.dfs((x, y), stack, visited, test_mode)

    def maze_directions(self, current_coordinates, neighbor_coordinates):
        """This method calls necessary visualization method from Maze class 
        based on which neighbor of the current cell was chosen. 
        Args:
            current_coordinates: Tuple that consists of current cell's coordinates.
            neighbor_coordinates: Tuple that consists of the neighbor's coordinates.
        """
        if neighbor_coordinates[0] > current_coordinates[0]:
            self.maze.right(current_coordinates[0], current_coordinates[1])

        elif neighbor_coordinates[0] < current_coordinates[0]:
            self.maze.left(current_coordinates[0], current_coordinates[1])

        elif neighbor_coordinates[1] > current_coordinates[1]:
            self.maze.down(current_coordinates[0], current_coordinates[1])

        elif neighbor_coordinates[1] < current_coordinates[1]:
            self.maze.up(current_coordinates[0], current_coordinates[1])

    def convert_to_coordinates(self, current):
        """This method converts cell position into its corresponding coordinates.
        Args:
            current: Tuple that has the position of the cell that is to be converted.
        """
        index = current[0]*self.maze.grid_size+current[1]
        coordinates = self.coordinates[index]
        return coordinates


#The source that was used to implement this dfs algorithm:
#https://courses.cs.washington.edu/courses/cse326/07su/prj2/kruskal.html
