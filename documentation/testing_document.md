# Testing document

## Unit tests

The testing is done using unittest library. Unit tests are done to classes that contain application logic or algorithms.    
Currently there are tests for DepthFirstSearch, DisjointSet and Kruskals classes.

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

![coverage_report](https://user-images.githubusercontent.com/102039234/232335730-53771fcf-7577-4cea-87c0-e9f0e8020995.png)



Coverage report can also be directly printed out with the following command.

```
poetry run coverage report -m
```
