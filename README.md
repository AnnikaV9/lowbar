
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

<br>

## Requirements
- Python 3.7 or above. lowbar may support earlier versions, but this has not been tested.
- A console that supports line feed `\n` and carriage return `\r`.

<br>

## Installation 
Install the latest stable release:
```
pip install lowbar
```
Or the development version:
```
pip install git+https://github.com/AnnikaV9/lowbar
```

<br>

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

The above function will immediately move the bar to 20%. To use a more smoother but slower animation:
```python3
bar.update_smooth(40)
```
***Note:** Since version 1.1.4, `update_smooth()` is no-longer fully blocking. It will run in a separate thread, so your program will continue it's execution while the bar is animating. However, calling another lowbar function during the animation will block the main thread to prevent visual glitches. To avoid this block, make sure to call `log()` before `update_smooth()`, not after. See issue [#5](https://github.com/AnnikaV9/lowbar/issues/5)*

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
    time.sleep(2) # This would be replaced with an actual task
    bar.log(f"Task {i+1} completed")
    completion += 10
    bar.update_smooth(completion)
bar.clear()

print("Tasks complete!")
```

You don't even need a loop:
```python3
bar = lowbar.lowbar()

bar.new()
time.sleep(1)
bar.update_smooth(10)
time.sleep(2)
bar.update_smooth(40)
time.sleep(2)
bar.update_smooth(100)
bar.clear()

print("Tasks complete!")
```

The bar can also be used with a context manager. It will automatically run `new()` at the start and `clear()` when exiting:
```python3
with lowbar.lowbar() as bar:
    time.sleep(1)
    bar.update_smooth(10)
    time.sleep(3)
    bar.update_smooth(100)

print("Tasks complete!")
```

To make things simpler, you can wrap lowbar around `range()` and turn it into an iterable. It will automatically calculate how much to increase the percentage by every loop:
```python3
for i in lowbar.lowbar(range(100)):
    time.sleep(0.5)
```

To make things even more simpler, you can pass an integer and lowbar will convert it into a range object for you:
```python3
for i in lowbar.lowbar(100):
    time.sleep(0.5)
```

lowbar will use `update()` by default when used as an iterable. If you're only going to loop a few times, you can force lowbar to use `update_smooth()`:
```python3
for i in lowbar.lowbar(6, smooth_iter=True):
    time.sleep(1)
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

<br>

## Parameters

- `__init__()` &nbsp; - &nbsp; **Init function thats called when the lowbar object is created.**

  - bar_iter: A range object that lowbar will iterate through when `__iter__()` is called. If an integer is provided, lowbar will automatically convert it into a range object. Default: `0`
  - smooth_iter: A boolean switch which forces lowbar to use `update_smooth()` when iterating. Default: `False`
  - bar_load_fill: A string of size 1, which will be used to fill the bar as it loads. Default: `"#"`
  - bar_blank_fill: A string of size 1, which will be used to fill the part of the bar that isn't loaded yet. Default: `"-"`
  - bar_desc: A string, which will be displayed to the left of the bar. If the console is too small to accommodate both the bar and the desc, the desc will be hidden. Default: `""`
  - remove_ends: A boolean switch which will hide the chars placed at both ends of the bar (`[` & `]`). Default: `False`
  - no_clear: A boolean switch which will stop lowbar from clearing the bar automatically when used as an iterable or with a context manager. Useful if you want a 'receipt'. Default: `False`

- `new()` &nbsp; - &nbsp; **Alias for `update(0)`**

- `update()` &nbsp; - &nbsp; **Increases or decreases the completed percentage and refreshes the bar, automatically resizing if the console size has changed.**

  - percentage: An integer value to set the completed percentage as. No default value.

- `update_smooth()` &nbsp; - &nbsp; **Same as `update()`, with a smoother but slower animation. Avoid using this function if execution speed is important for you. The completion percentage cannot be decreased with this function.**

  - percentage: An integer value to set the completed percentage as. Must be higher than the currently set value. No default value.

- `log()` &nbsp; - &nbsp; **Logs text to the console without affecting the bar.**

  - text: Any string. Any other type needs to be converted with `str()` before being passed to this function. No default value.

- `clear()` &nbsp; - &nbsp; **Clears the currently running bar.**

<br>

## Contributing
All contributions are welcome!

If you wish to report a bug or suggest a feature, open an [issue](https://github.com/AnnikaV9/lowbar/issues).

You can also make a [pull request](https://github.com/AnnikaV9/lowbar/pulls) directly if you already have the fix for a bug.

See [CONTRIBUTING.md](https://github.com/AnnikaV9/lowbar/blob/master/CONTRIBUTING.md) for guidelines to follow.

Contributors are listed in [CONTRIBUTORS.md](https://github.com/AnnikaV9/lowbar/blob/master/CONTRIBUTORS.md).

<br>

## License
```
MIT License

Copyright (c) 2022 AnnikaV9

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
