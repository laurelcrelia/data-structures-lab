# Testing document

## Unit tests

The testing is done using unittest library.     
Unit tests are done to classes `Kruskals`, `DepthFirstSearch` and `DisjointSet`.

Tests and coverage report can be executed with the following command.

```
poetry run coverage run --branch -m pytest src
```

## Coverage report

HTML report of coverage is written with command
```
poetry run coverage html
```
Now the coverage report is found at htmlcov/index.html.    

![Screenshot from 2023-05-12 21-16-11](https://github.com/laurelcrelia/data-structures-lab/assets/102039234/9223dbba-ce0e-4442-950c-664445958afa)

Note that both Kruskals and DepthFirstSearch classes have following five rows of pygame code that is not included in tests:   
    
![Screenshot from 2023-05-14 12-59-19](https://github.com/laurelcrelia/data-structures-lab/assets/102039234/efac2b2c-8f0f-4b65-8444-33500cddb1ab)       
This lowers the coverage rate a little bit.   


Coverage report can also be directly printed out with the following command.

```
poetry run coverage report -m
```

## Comparative analysis
In this case the performance comparison is not so relevant. Instead the visual analysis could be discussed.
The following pictures show some generatings from the program.    

![5x5 maze](https://github.com/laurelcrelia/data-structures-lab/assets/102039234/355d88ff-c727-48ba-8e40-215418ce8f30)
![10x10 maze](https://github.com/laurelcrelia/data-structures-lab/assets/102039234/ae9f42dd-e000-4e63-a773-318f7aee2ca9)
![20x20 maze](https://github.com/laurelcrelia/data-structures-lab/assets/102039234/8a1560d9-226d-4b52-8e72-4f862c752e53)

The first mazes (5x5) usually seem quite similar, but with bigger maze sizes the difference becomes clearer.
Depth-first search seems to generally make longer corridors, while Kruskal's algorithm generates many short dead-ends.
Reason to this is that DFS algorithm works by searching as far as possible along each branch before backtracking. 
Unlike Kruskal's algorithm randomly explores a new cell from the maze on every round.

Visually, DFS may look more pleasing to the eye, but Kruskal's mazes are generally a bit more complex and thus harder to solve.

