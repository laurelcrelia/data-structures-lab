# Testing document

## Unit tests

The testing is done using unittest library. Unit tests are done to classes that contain application logic or algorithms.    
Currently there are only tests for the ```dfs.py``` file.

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

![coverage_report](https://user-images.githubusercontent.com/102039234/231878972-236b2cbe-e38c-4b8b-bcef-a48924ca4006.png)



Coverage report can also be directly printed out with the following command.

```
poetry run coverage report -m
```
