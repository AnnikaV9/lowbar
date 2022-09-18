<div align="center">
<h1>
lowbar<br />
<a target="_blank" href="https://pypi.org/project/lowbar"><img src="https://img.shields.io/pypi/v/lowbar?label=PyPi&color=red"></a> <a target="_blank" href="https://github.com/AnnikaV9/lowbar/blob/master/LICENSE" title="License"><img src="https://img.shields.io/github/license/AnnikaV9/lowbar?label=License&color=blue"></a> <a target="_blank" href="https://github.com/AnnikaV9/lowbar/actions/workflows/flake8.yml"><img src="https://github.com/AnnikaV9/lowbar/actions/workflows/flake8.yml/badge.svg"></a>
</h1>

The simplest no-nonsense progress bar for python
<br /><br />
<img src="https://user-images.githubusercontent.com/68383195/190890215-7b450696-dcd1-4911-b6e8-034d5fdf48c0.gif"><br />
</div>

<br />
<br />

## Introduction
lowbar is a blazing fast module with zero dependencies for displaying a progress bar in the terminal. It has a low number of features and a simple codebase, hence the name lowbar.

<br />
<br />

## Installation 
Install the latest stable release:
```
pip install lowbar
```
<br />

Or the development version (Undocumented):
```
pip install git+https://github.com/AnnikaV9/lowbar
```

<br />
<br />

## Usage

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

To make things even more simpler, you can wrap lowbar around an iterable. It will automatically calculate how much to increase the percentage by every loop:
```python3
for i in lowbar.lowbar(range(100)):
    time.sleep(0.5)
```

<br />

lowbar will use `update()` by default when working with iterables. If you're only going to loop a few times, you can force lowbar to use `update_smooth()`:
```python3
for i in lowbar.lowbar(range(6), smooth_iter=True):
    time.sleep(1)
```
***Note:** You can't use `log()` when using lowbar with an iterable.*

<br />

You can change the load fill and blank fill chars as well:
```python3
bar = lowbar.lowbar(bar_load_fill="O", bar_blank_fill=".")
```

<br />
<br />

## Contributing
All contributions are welcome!

If you wish to report a bug or suggest a feature, open an [issue](https://github.com/AnnikaV9/lowbar/issues).

If you already have a fix for a bug, make a [pull request](https://github.com/AnnikaV9/lowbar/pulls) directly.

You can also [vote on](https://github.com/AnnikaV9/lowbar/discussions/4) already suggested features.

See [CONTRIBUTING.md](https://github.com/AnnikaV9/lowbar/blob/master/CONTRIBUTING.md) for guidelines to follow.

Contributors are listed in [CONTRIBUTORS.md](https://github.com/AnnikaV9/lowbar/blob/master/CONTRIBUTORS.md).

<br />
<br />

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
