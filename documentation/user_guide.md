## Installation instructions

1. Clone this repository into your computer

2. Install dependencies in project's root directory with command    
`poetry install`    
   
3. Activate the virtual environment with command   
`poetry shell`    
    
4. Start the program with command    
`python3 src/index.py`

## User guide
    
After user has chosen a grid size for mazes, the program starts generating mazes one at a time.
Once the first algorithm (Kruskal's) is ready then the second one (Depht-first search) starts generating its maze.

You can test the quality of the code with command   
`pylint src`    

Unit tests and coverage are invoked with command    
`coverage run --branch -m pytest src`   

Coverage report gets printed out with command   
`coverage report -m`    
 
