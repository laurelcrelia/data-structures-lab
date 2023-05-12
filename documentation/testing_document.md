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




Coverage report can also be directly printed out with the following command.

```
poetry run coverage report -m
```
