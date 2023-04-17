# Maze generator

![GHA workflow badge](https://github.com/laurelcrelia/data-structures-lab/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/laurelcrelia/data-structures-lab/branch/main/graph/badge.svg?token=XSGKMVPU1C)](https://codecov.io/gh/laurelcrelia/data-structures-lab)

Project for Data Structures Lab course at the University of Helsinki.

### Documentation:
- [Project specification](https://github.com/laurelcrelia/data-structures-lab/blob/main/documentation/project-specification.md)
- [Testing document](https://github.com/laurelcrelia/data-structures-lab/blob/main/documentation/testing_document.md)
- [Implementation document](https://github.com/laurelcrelia/data-structures-lab/blob/main/documentation/implementation_document.md)

### Weekly reports:
- [Week 1](https://github.com/laurelcrelia/data-structures-lab/blob/main/documentation/weekly_reports/week1.md)
- [Week 2](https://github.com/laurelcrelia/data-structures-lab/blob/main/documentation/weekly_reports/week2.md)
- [Week 3](https://github.com/laurelcrelia/data-structures-lab/blob/main/documentation/weekly_reports/week3.md)
- [Week 4](https://github.com/laurelcrelia/data-structures-lab/blob/main/documentation/weekly_reports/week4.md)

## User instructions

After cloning this repository into your computer install dependencies in project's root directory with command    
`poetry install`    
    
Activate the virtual environment with command   
`poetry shell`    
    
Start the program with command    
`python3 src/index.py`    
    
At the moment the main part of the program works like this:
- After user has chosen a grid size for mazes, the program starts generating mazes one at a time.
Once the first algorithm (Kruskal's) is ready then the second one (Depht-first search) starts generating its maze.
- The last grid size (20) leads to 'maximum recursion depth exceeded'- error with dfs algorithm.

You can test the quality of the code with command   
`pylint src`    

Unit tests and coverage are invoked with command    
`coverage run --branch -m pytest src`   

Coverage report gets printed out with command   
`coverage report -m`    
 

