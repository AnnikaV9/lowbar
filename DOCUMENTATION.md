## Usage

<br />

Once you have lowbar in your project, you can import it like any other module:
```python3
import lowbar
```

<br />

And initialize the bar:
```python3
bar = lowbar.lowbar()
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
bar = lowbar.lowbar()
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
bar = lowbar.lowbar()
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
<br />

<div align="center">
<a href="INSTALLATION.md">Installation</a> &nbsp; | &nbsp;
<a href="https://github.com/AnnikaV9/lowbar">Home</a> &nbsp; | &nbsp;
<a href="LICENSE">License</a>
</div>