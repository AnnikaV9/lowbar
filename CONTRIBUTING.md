# Contributing
A set of guidelines to follow when contributing to lowbar.

<br />
<br />

## Keep code complexity minimal
lowbar's main goal is to be a **simple** solution that is bug-free and easily maintained. Extremly complex or spaghetti code makes the codebase harder to maintain, and increases the possibilities of bugs in future updates.

<br />
<br />

## Consistent styling, annotation and syntax

Variable and function names should be written in [snake case](https://en.wikipedia.org/wiki/Snake_case):
```python3
my_var
my_func()
```

<br />

Add docstrings to functions:
```python3
def my_func(self, arg1: str, arg2: int):

    """
    blah blah
    """

    // code //
```

<br />

Annotate variables when defining them:
```python3
my_var1: str = "blah blah"
my_var2: int = 99
```

<br />

Specify function return value types:
```python3
def my_func(self, arg1: str, arg2: int) -> list:
   
   // code//
   
   return my_list
```

<br />
<br />

## No dependencies apart from the Python Standard Library
Check [docs.python.org/3/library/index.html](https://docs.python.org/3/library/index.html) for reference.
