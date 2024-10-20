
# lowbar
The simplest no-nonsense progress bar for python.

![Preview GIF](https://github.com/user-attachments/assets/335b85ae-5bdf-48cc-9192-d63770aeb17b)

lowbar is a blazing fast module with zero dependencies for displaying a progress bar in the terminal. It has a low number of features and a simple codebase, hence the name lowbar.

#### lowbar has:
- Automatic resizing
- Manual progress management
- Automatic progress management (As an iterable)
- Text logging
- Bar styling
- Low overhead
- Small size ( < 150 lines)

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
from lowbar import lowbar
```

And initialize the bar:
```python3
bar = lowbar()
```

To make the bar visible and set at 0%:
```python3
bar.new()
```

After completing some tasks, we can increase the bar's completion percentage:
```python3
bar.add(20)
```

If we have a known number of tasks, lowbar can automatically calculate the percentage for us:
```python3
bar.next(n_tasks)
```
> [!NOTE]
> If you set the number of tasks when initializing lowbar with `lowbar(n_tasks)`, you don't need to pass `n_tasks` to `next()`.

We can also set the completion percentage instead of adding to it:
```python3
bar.update(50)
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
bar = lowbar(10)
bar.new()
for i in range(10):
    time.sleep(0.5)  # task
    bar.log(f"Task {i+1} completed")
    bar.next()
bar.clear()

print("Tasks complete!")
```

You don't even need a loop:
```python3
bar.new()
time.sleep(0.5)  # task
bar.add(10)
time.sleep(0.5)  # task
bar.add(10)
time.sleep(0.5)  # task
bar.update(100)
bar.clear()

print("Tasks complete!")
```

The bar can also be used with a context manager. It will automatically run `new()` at the start and `clear()` when exiting:
```python3
with lowbar(2) as bar:
    time.sleep(0.5)  # task
    bar.next()
    time.sleep(0.5)  # task
    bar.next()

print("Tasks complete!")
```

To make things simpler, you can wrap lowbar around `range()` and turn it into an iterable. It will automatically calculate how much to increase the percentage by every loop:
```python3
for i in lowbar(range(100)):
    time.sleep(0.5)  # task
```

Pass an integer and lowbar will convert it into a range object for you:
```python3
for i in lowbar(100):
    time.sleep(0.5)  # task
```
> [!NOTE]
> You can't use `log()` when using lowbar as an iterable.

You can also change the load fill and blank fill chars:
```python3
bar = lowbar(load_fill="O", blank_fill=".")
```

Or add a description text to the left side of the bar:
```python3
bar = lowbar(desc="Downloading...")
```
> [!NOTE]
> If the console is too small to accommodate both the bar and the description text, the text will be hidden.

<br>

**See the [reference](https://github.com/AnnikaV9/lowbar/wiki/Reference) for more details.**

## Contributing
All contributions are welcome!

If you wish to report a bug or suggest a feature, open an [issue](https://github.com/AnnikaV9/lowbar/issues).

You can also make a [pull request](https://github.com/AnnikaV9/lowbar/pulls) directly if you already have the fix for a bug.

See [CONTRIBUTING.md](../docs/CONTRIBUTING.md) for guidelines to follow.

Contributors are listed in [CONTRIBUTORS.md](../docs/CONTRIBUTORS.md).

## License
This project is licensed under the [MIT License](../LICENSE).
