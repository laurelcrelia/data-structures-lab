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
        Sets up all needed data structures e.g. stack and lists."""

        self.maze = maze

        self.x_axis = self.maze.x_axis_1
        self.y_axis = self.maze.y_axis
        self.cell_size = 40/(self.maze.grid_size/5)

        self.stack = []

        self.cells = []
        self.neighbors = []
        self.visited = []

    def initialize_cells(self):
        """This method initializes cells by adding all existing cells to a list."""
        for i in range(self.maze.grid_size):
            for j in range(1, self.maze.grid_size+1):
                self.cells.append((self.x_axis+(i*self.cell_size), self.y_axis+(j*self.cell_size)))

    def choose_cell(self):
        """This method chooses a random cell from the list of all cells"""
        chosen_cell = random.choice(self.cells)
        return chosen_cell

    def find_neighbors(self, x_axis, y_axis):
        """This method picks the neighbors of the current cell
        that have all their walls up i.e. are unvisited and adds them to 
        neighbors -list.
        Args:
            x_axis: Variable that determines the x coordinate of the current cell.
            y_axis: Variable that determines the y coordinate of the current cell.
        """
        self.neighbors.clear()

        right_neighbor = (x_axis + self.cell_size, y_axis)
        left_neighbor = (x_axis - self.cell_size, y_axis)
        lower_neighbor = (x_axis , y_axis + self.cell_size)
        upper_neighbor = (x_axis, y_axis - self.cell_size)

        if right_neighbor not in self.visited and right_neighbor in self.cells:
            self.neighbors.append("right")

        if left_neighbor not in self.visited and left_neighbor in self.cells:
            self.neighbors.append("left")

        if lower_neighbor not in self.visited and lower_neighbor in self.cells:
            self.neighbors.append("down")

        if upper_neighbor not in self.visited and upper_neighbor in self.cells:
            self.neighbors.append("up")

    def recursion(self, x_axis, y_axis):
        """This is the recursive function of DFS.

        Args:
            x_axis: Variable that determines x coordinate of the current cell.
            y_axis: Variable that determines y coordinate of the current cell.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

            self.find_neighbors(x_axis, y_axis)

            if len(self.neighbors) > 0:
                self.next_neighbor(x_axis, y_axis)

            else:
                if len(self.stack) > 0:
                    self.backtrack(x_axis, y_axis)

    def next_neighbor(self, x_axis, y_axis):
        """This method is called from recursion method when there is a need to 
        knock down a wall between current and neighbor.

        Args:
            x_axis: Variable that determines x coordinate of the current cell.
            y_axis: Variable that determines y coordinate of the current cell.
        """
        chosen_neighbor = random.choice(self.neighbors)

        self.visit_cell(x_axis, y_axis)
        self.stack.append((x_axis, y_axis))

        new_x = x_axis
        new_y = y_axis

        if chosen_neighbor == "right":
            self.maze.right(x_axis, y_axis)
            new_x = x_axis + self.cell_size

        elif chosen_neighbor == "left":
            self.maze.left(x_axis, y_axis)
            new_x = x_axis - self.cell_size

        elif chosen_neighbor == "down":
            self.maze.down(x_axis, y_axis)
            new_y = y_axis + self.cell_size

        elif chosen_neighbor == "up":
            self.maze.up(x_axis, y_axis)
            new_y = y_axis - self.cell_size

        self.visit_cell(new_x, new_y)
        self.recursion(new_x,new_y)

    def visit_cell(self, x_axis, y_axis):
        """This method marks given cell visited by adding it to a visited list."""
        self.visited.append((x_axis, y_axis))

    def backtrack(self, x_axis, y_axis):
        """This method is called from recursion method when backtracking needs to take place.
        This method pops current cell off of the stack and calls backtracking_cell() 
        which in turn will call recursion method after it has drawn the track to the maze.

        Args:
            x_axis: Variable that determines x coordinate of the current cell.
            y_axis: Variable that determines y coordinate of the current cell.
        """
        x_axis, y_axis = self.stack.pop()
        self.maze.current_cell(x_axis, y_axis)
        self.maze.backtracking_cell(x_axis, y_axis)
        self.recursion(x_axis, y_axis)


#The source that was used to implement this dfs algorithm:
#https://courses.cs.washington.edu/courses/cse326/07su/prj2/kruskal.html
