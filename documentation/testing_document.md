# Testing document

## Unit tests

The testing is done using unittest library. Unit tests are done to classes that contain application logic or algorithms.    
Currently there are only tests for DepthFirstSearch and DisjointSet classes.

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

![coverage_report](https://user-images.githubusercontent.com/102039234/232315783-bf6f6ee2-4f9f-494f-a69c-87bd6664b913.png)



Coverage report can also be directly printed out with the following command.

```
poetry run coverage report -m
```
