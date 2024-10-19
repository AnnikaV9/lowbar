
# lowbar
[![](https://img.shields.io/github/actions/workflow/status/AnnikaV9/lowbar/flake8.yml?label=Flake8)](https://github.com/AnnikaV9/lowbar/actions/workflows/flake8.yml)
[![](https://img.shields.io/pypi/v/lowbar?label=PyPi&color=blue)](https://pypi.org/project/lowbar)
[![](https://img.shields.io/github/license/AnnikaV9/lowbar?label=License&color=blue)](https://github.com/AnnikaV9/lowbar/blob/master/LICENSE)
[![](https://img.shields.io/badge/Python->=3.7-blue)](https://pypi.org/project/lowbar)
[![](https://img.shields.io/github/languages/code-size/AnnikaV9/lowbar?label=Code%20Size)](https://github.com/AnnikaV9/lowbar/blob/master/src/lowbar/__init__.py)
[![](https://static.pepy.tech/personalized-badge/lowbar?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/lowbar)

The simplest no-nonsense progress bar for python.


![demo](https://user-images.githubusercontent.com/68383195/192450722-9a98f90a-ae0f-4079-a1e0-c37c597cce82.gif)


lowbar is a blazing fast module with zero dependencies for displaying a progress bar in the terminal. It has a low number of features and a simple codebase, hence the name lowbar.

#### lowbar has:
- Automatic resizing
- Manual progress management
- Automatic progress management (As an iterable)
- Text logging
- Bar customization
- Extremely low overhead
- Small package size

#### lowbar doesn't have:
- Nested bars
- Fancy animations
- ETA calculations

## Requirements
- Python 3.7 or above. lowbar may support earlier versions, but this has not been tested.
- A console that supports line feed `\n` and carriage return `\r`.

## Installation
Install the latest stable release:
```
pip install lowbar
```
Or the development version:
```
pip install git+https://github.com/AnnikaV9/lowbar
```

## Usage
Once you have lowbar installed, you can import it like any other module:
```python3
import lowbar
```

And initialize the bar:
```python3
bar = lowbar.lowbar()
```

To make the bar visible and set at 0%:
```python3
bar.new()
```

After completing some tasks, we can increase the bar's completion percentage:
```python3
bar.update(20)
```

Using `print()` or other similar functions will push the bar up, which doesn't look nice. To log messages without affecting the bar:
```python3
bar.log("Hello World!")
```

And finally, to clear the bar completely:
```python3
bar.clear()
```

Here's an example usage of the bar:
```python3
bar = lowbar.lowbar()

completion = 0
bar.new()
for i in range(10):
    time.sleep(2)  # task
    bar.log(f"Task {i+1} completed")
    completion += 10
    bar.update(completion)
bar.clear()

print("Tasks complete!")
```

You don't even need a loop:
```python3
bar = lowbar.lowbar()

bar.new()
time.sleep(1)  # task
bar.update(10)
time.sleep(2)  # task
bar.update(40)
time.sleep(2)  # task
bar.update(100)
bar.clear()

print("Tasks complete!")
```

The bar can also be used with a context manager. It will automatically run `new()` at the start and `clear()` when exiting:
```python3
with lowbar.lowbar() as bar:
    time.sleep(1)  # task
    bar.update(10)
    time.sleep(3)  # task
    bar.update(100)

print("Tasks complete!")
```

To make things simpler, you can wrap lowbar around `range()` and turn it into an iterable. It will automatically calculate how much to increase the percentage by every loop:
```python3
for i in lowbar.lowbar(range(100)):
    time.sleep(0.5)  # task
```

To make things even more simpler, you can pass an integer and lowbar will convert it into a range object for you:
```python3
for i in lowbar.lowbar(100):
    time.sleep(0.5)  # task
```
> [!NOTE]
> You can't use `log()` when using lowbar as an iterable.

You can also change the load fill and blank fill chars:
```python3
bar = lowbar.lowbar(bar_load_fill="O", bar_blank_fill=".")
```

Or add a description text to the left side of the bar:
```python3
bar = lowbar.lowbar(bar_desc="Downloading...")
```
> [!NOTE]
> If the console is too small to accommodate both the bar and the description text, the text will be hidden.

## Parameters

#### `__init__()`
Called when the `lowbar` object is created.

| Parameter         | Type    | Description                                                                                                                   | Default  |
|-------------------|---------|-------------------------------------------------------------------------------------------------------------------------------|----------|
| `bar_iter`        | `range` | A range object that `lowbar` will iterate through when `__iter__()` is called. If an integer is provided, `lowbar` converts it into a range object. | `0`      |
| `bar_load_fill`   | `str`   | A single-character string used to fill the bar as it loads.                                                                    | `"#"`    |
| `bar_blank_fill`  | `str`   | A single-character string used to fill the unloaded part of the bar.                                                           | `"-"`    |
| `bar_desc`        | `str`   | Text displayed to the left of the bar. If the console is too small, this text will be hidden.                                  | `""`     |
| `remove_ends`     | `bool`  | Hides the characters at both ends of the bar (`[` & `]`).                                                                      | `False`  |
| `no_clear`        | `bool`  | Prevents `lowbar` from automatically clearing the bar after completion (useful for keeping the progress bar as a 'receipt').   | `False`  |

#### `new()`
Alias for `update(0)`.

#### `update()`
Increases or decreases the completed percentage and refreshes the bar, resizing if the console size changes.

| Parameter    | Type   | Description                                      | Default         |
|--------------|--------|--------------------------------------------------|-----------------|
| `percentage` | `int`  | The percentage to set as the completed progress. | *No default*    |

#### `log()`
Logs text to the console without affecting the bar.

| Parameter    | Type   | Description                                                             | Default         |
|--------------|--------|-------------------------------------------------------------------------|-----------------|
| `text`       | `str`  | The text to log. Other types must be converted to strings before logging.| *No default*    |

#### `clear()`
Clears the currently active bar.

## Contributing
All contributions are welcome!

If you wish to report a bug or suggest a feature, open an [issue](https://github.com/AnnikaV9/lowbar/issues).

You can also make a [pull request](https://github.com/AnnikaV9/lowbar/pulls) directly if you already have the fix for a bug.

See [CONTRIBUTING.md](../docs/CONTRIBUTING.md) for guidelines to follow.

Contributors are listed in [CONTRIBUTORS.md](../docs/CONTRIBUTORS.md).

## License
This project is licensed under the [MIT License](LICENSE).
