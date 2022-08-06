<div align="center">
<h1>
lowbar<br />
<a target="_blank" href="pyproject.toml" title="Version"><img src="https://img.shields.io/static/v1?label=Version&message=0.1.7&color=red"></a> <a target="_blank" href="LICENSE" title="License"><img src="https://img.shields.io/static/v1?label=License&message=The%20Unlicense&color=blue"></a> <a target="_blank" href="https://github.com/AnnikaV9/lowbar/actions/workflows/pylint.yml"><img src="https://github.com/AnnikaV9/lowbar/actions/workflows/pylint.yml/badge.svg"></a>
</h1>

The simplest no-nonsense loading bar for python.
<br /><br />
<img src="https://user-images.githubusercontent.com/68383195/183113043-7a891444-bf5a-45eb-af39-336e609a2c96.gif" width="80%">
<br /><br /><details>
<summary><em>demo.py</em></summary>
<div align="left">
<br /><pre>
<code># All the sleep calls would be tasks to
# complete in a real program
<br />
import lowbar, time, random
<br />
bar = lowbar.LowBar()
<br />
completion = 0
<br />
for i in range(10):
    time.sleep(random.random())
    bar.update_smooth(completion)
    bar.log(f"Task {i+1} completed")
    completion += 10
bar.clear()
<br />
print("\nRunning checks...")
bar.update(0)
time.sleep(1)
bar.update_smooth(10)
time.sleep(2)
bar.update_smooth(40)
time.sleep(2)
bar.update_smooth(100)
bar.clear()
print("Tasks complete!")</code></pre>
</div>
</details>
<h3>

<h3>
</div>
<br />
<br />

## Installation 
Install the latest stable release:
```
pip install lowbar
```
<br />

Or build the development version in this repository:
```
pip install build hatchling
python3 -m build -w
pip install dist/lowbar-*-py3-none-any.whl
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
bar = lowbar.LowBar()
```

<br />

To make the bar visible, simple update the completion percentage:
```python3
bar.update(0)
```
*We start with 0 since our program hasn't completed anything yet.*

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
import lowbar, time
bar = lowbar.LowBar()
completion = 0
for i in range(10):
    time.sleep(2) # This would be replaced with an actual task
    bar.update_smooth(completion)
    bar.log(f"Task {i+1} completed")
    completion += 10
bar.clear()
print("Tasks complete!")
```

<br />

You don't even need a loop:
```python3
import lowbar, time
bar = lowbar.LowBar()
bar.update(0)
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

You can change the load fill and blank fill chars as well:
```python3
bar = lowbar.LowBar(bar_load_fill="O", bar_blank_fill=".")
```

<br />
<br />

## Contributing
All contributions are welcome!

If you wish to to report a bug or suggest a feature, open an [issue](https://github.com/AnnikaV9/lowbar/issues).

You can also make a [pull request](https://github.com/AnnikaV9/lowbar/pulls) directly.

<br />
<br />

## License

```
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
```
