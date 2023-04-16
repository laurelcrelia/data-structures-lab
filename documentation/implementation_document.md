# Implementation document

## Project structure

At the moment the project has following classes:    
- `App` controls the switching between different user interface stages.
- `Call` invokes the algorithms.
- `DepthFirstSearch` creates the depth-first search algorithm.    
- `DisjointSet` creates the disjoint set data structure that is needed for Kruskal's algorithm.  
- `Kruskals` creates the Kruskal's algorithm.      
- `Stage` helps different user interface stages to operate by initializing the screen, controlling the widgets and creating a pygame mainloop. 
  
In addition there is `app.py` file which starts the program, a `tests` directory which contains unit tests and `ui` directory which consists of all files that create the user interface.

## Implemented time and space complexities
--

## Possible flaws and improvements
--
