# Implementation document

## Project structure

At the moment the project has following classes:    
- `App` controls the switching between different user interface stages.
- `Call` invokes the algorithms.
- `DepthFirstSearch` creates the depth-first search algorithm.    
- `DisjointSet` creates the disjoint set data structure that is needed for Kruskal's algorithm.  
- `Kruskals` creates the Kruskal's algorithm.      
- `Stage` helps different user interface stages to operate by initializing the screen, controlling the widgets and creating a pygame mainloop. 
  
In addition there is `index.py` file which starts the program, a `tests` directory which contains unit tests and `ui` directory which consists of all files that create the user interface.

## Implemented time and space complexities

In the following instances, E is the amount of edges and V is the amount of vertices in the graph. The number of cells in a maze is expressed with n. 
The number of edges is proportional to the number of cells E = O(n). V is at most E+1.

Kruskal’s algorithm is a sorting algorithm with a time complexity of **O(n log n)**. Although Kruskal’s algorithm uses disjoint set data structures where each "find" and "union" operation is O(log V), the total time complexity is O(E log E + E log V).     
This simplifies to O(n log n), since E is the same as n and V is at most E+1, and the standard coefficients and lower terms do not affect the time required.

The time complexity of a DFS is **O(n)**. In the worst case, the DFS visits every cell, and therefore makes n recursive calls.    
Each recursive call takes constant time, since the maze is represented as a two-dimensional array.

The space complexity of both algorithms is **O(n)**. Kruskal’s has to store the edges and the disjoint sets data structure, which both require O(n) space. With DFS, in the worst case, where it visits every cell, its stack has to store O(n) elements.

## Possible flaws and improvements
Changes or new features:
- There could be more grid size options where to choose from or the user could insert their own desired integer input. 
- Both algorithms could generate their mazes at the same time or at least the visualization could happen at the same time.
- Once the mazes are created, a button appears that could activate a feature that shows the solution path. This would require a pathfinding algorithm. DFS could do this too.

## Sources
The algorithms were implemented according to the pseudocodes on [this](https://courses.cs.washington.edu/courses/cse326/07su/prj2/kruskal.html) site.   
The disjoint-set data structure was created by the help of the examples on [this](https://www.geeksforgeeks.org/disjoint-set-data-structures/) site.
