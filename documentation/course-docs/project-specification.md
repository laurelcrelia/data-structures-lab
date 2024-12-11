# Project specification

The programming language used in this project is Python. The language of documentation, code and comments is English.

My degree programme is Bachelor’s in Computer Science.

In this program I will compare two maze generating algorithms. I came across this topic when making my Ohjelmistotekniikka -course project last year. 
My OhTe project was a very primitive maze type game and I figured it takes a lot of time to make every level of the game by hand. 
This OhTe project was a very small project and creating an algorithm wasn’t essential then, but if I wanted to implement the idea on a bigger scale in future, it would become necessary to generate new levels by some algorithm. 

### Algorithms
The algorithms that I will compare are randomized **depth-first search** and randomized **Kruskal’s algorithm**. 
I chose depth-first search (also known as Recursive Backtracking) because it is fast and straightforward. Kruskal’s algorithm on the other hand is a greedy algorithm and doesn't work too well on bigger mazes. I expect the two algorithms to produce results with differences concerning visual outcome of the maze.

### Data structures
The maze can be viewed as a graph. The nodes can be stored in a two-dimensional array and adjacency list describes the connections (edges) between the nodes. 
Depth-first search uses also a stack to help with backtracking on a graph. Kruskal’s algorithm uses disjoint set data structures.

### Input
User can choose a grid size from three different options and the program starts generating Kruskal's and DFS mazes accordingly. 

### Expected time and space complexities
For a graph with E edges and V vertices, the time complexity of DFS is O(|V| + |E|). Space complexity of DFS is O(|V|).   
The expected time complexity of Kruskal’s algorithm is O(E log V). Space complexity of Kruskal’s algorithm is O(|E| + |V|).

## Sources
- [Wikipedia: Maze generation algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm)   
- [Wikipedia: Depth-first search algorithm](https://en.wikipedia.org/wiki/Depth-first_search)   
- [Wikipedia: Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)   
- [The Buckblog by Jamis Buck: Recursive Backtracking](https://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracking)    
- [The Buckblog by Jamis Buck: Kruskal's algorithm](https://weblog.jamisbuck.org/2011/1/3/maze-generation-kruskal-s-algorithm)
