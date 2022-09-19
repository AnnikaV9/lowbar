
# lowbar
[![](https://img.shields.io/github/workflow/status/AnnikaV9/lowbar/Flake8?label=Flake8)](https://github.com/AnnikaV9/lowbar/actions/workflows/flake8.yml)
[![](https://img.shields.io/pypi/v/lowbar?label=PyPi&color=blue)](https://pypi.org/project/lowbar)
[![](https://img.shields.io/github/license/AnnikaV9/lowbar?label=License&color=blue)](https://github.com/AnnikaV9/lowbar/blob/master/LICENSE)
[![](https://img.shields.io/badge/Python->=3.7-blue)](https://pypi.org/project/lowbar)
[![](https://img.shields.io/github/languages/code-size/AnnikaV9/lowbar?label=Code%20Size)](https://github.com/AnnikaV9/lowbar/blob/master/src/lowbar/__init__.py)
[![](https://static.pepy.tech/personalized-badge/lowbar?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/lowbar)

The simplest no-nonsense progress bar for python.


![demo](https://user-images.githubusercontent.com/68383195/191001041-1018bc7c-57a1-4ae9-9ee9-8de84296a11a.gif)


lowbar is a blazing fast module with zero dependencies for displaying a progress bar in the terminal. It has a low number of features and a simple codebase, hence the name lowbar.

<br />

#### lowbar has:
- Automatic resizing
- Manual progress management
- Automatic progress management (As an iterable)
- Text logging
- Extremely low overhead
- Small package size

#### lowbar doesn't have:
- Nested bars
- Fancy animations
- ETA calculations

<br />

## Requirements

<br />

- Python 3.7 or above. lowbar may support earlier versions, but this has not been tested.
- A console that supports line feed `\n` and carriage return `\r`.

<br />

## Installation 

<br />

Install the latest stable release:
```
pip install lowbar
```

<br />

Or the development version:
```
pip install git+https://github.com/AnnikaV9/lowbar
```

<br />

## Usage

<br />

Once you have lowbar installed, you can import it like any other module:
```python3
import lowbar
```

<br />

And initialize the bar:
```python3
bar = lowbar.lowbar()
```

<br />

To make the bar visible and set at 0%:
```python3
bar.new()
```

<br />

After completing some tasks, we can increase the bar's completion percentage:
```python3
bar.update(20)
```

<br />

The above function will immediately move the bar to 20%. To use a more smoother but slower animation:
```python3
bar.update_smooth(40)
```
***Note:** Since version 1.1.4, `update_smooth()` is no-longer fully blocking. It will run in a separate thread, so your program will continue it's execution while the bar is animating. However, calling another lowbar function during the animation will block the main thread to prevent visual glitches. To avoid this block, make sure to call `log()` before `update_smooth()`, not after. See issue [#5](https://github.com/AnnikaV9/lowbar/issues/5)*

<br />

Using `print()` or other similar functions will push the bar up, which doesn't look nice. To log messages without affecting the bar:
```python3
bar.log("Hello World!")
```

<br />

And finally, to clear the bar completely:
```python3
bar.clear()
```

<br />

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

<br />

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

<br />

The bar can also be used with a context manager. It will automatically run `new()` at the start and `clear()` when exiting:
```python3
with lowbar.lowbar() as bar:
    time.sleep(1)
    bar.update_smooth(10)
    time.sleep(3)
    bar.update_smooth(100)

print("Tasks complete!")
```

<br />

To make things simpler, you can wrap lowbar around `range()` and turn it into an iterable. It will automatically calculate how much to increase the percentage by every loop:
```python3
for i in lowbar.lowbar(range(100)):
    time.sleep(0.5)
```

<br />

To make things even more simpler, you can pass an integer and lowbar will convert it into a range object for you:
```python3
for i in lowbar.lowbar(100):
    time.sleep(0.5)
```
<br />

lowbar will use `update()` by default when used as an iterable. If you're only going to loop a few times, you can force lowbar to use `update_smooth()`:
```python3
for i in lowbar.lowbar(6, smooth_iter=True):
    time.sleep(1)
```
***Note:** You can't use `log()` when using lowbar as an iterable.*

<br />

You can also change the load fill and blank fill chars:
```python3
bar = lowbar.lowbar(bar_load_fill="O", bar_blank_fill=".")
```

<br />

## Contributing

<br />

All contributions are welcome!

If you wish to report a bug or suggest a feature, open an [issue](https://github.com/AnnikaV9/lowbar/issues).

If you already have a fix for a bug, make a [pull request](https://github.com/AnnikaV9/lowbar/pulls) directly.

You can also [vote on](https://github.com/AnnikaV9/lowbar/discussions/4) already suggested features.

See [CONTRIBUTING.md](https://github.com/AnnikaV9/lowbar/blob/master/CONTRIBUTING.md) for guidelines to follow.

Contributors are listed in [CONTRIBUTORS.md](https://github.com/AnnikaV9/lowbar/blob/master/CONTRIBUTORS.md).

<br />

## License

<br />

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
