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

![Screenshot from 2023-04-30 14-26-27](https://user-images.githubusercontent.com/102039234/235350496-c9de311b-8ee0-4dd5-8611-87ab64ba55dc.png)



Coverage report can also be directly printed out with the following command.

```
poetry run coverage report -m
```
