<div align="center">
<h1>
lowbar<br />
<a target="_blank" href="src/lowbar/lowbar.py" title="Lines"><img src="https://img.shields.io/static/v1?label=Lines&message=61&color=green&style=flat-square"></a> <a target="_blank" href="LICENSE" title="License"><img src="https://img.shields.io/static/v1?label=License&message=The%20Unlicense&color=blue&style=flat-square"></a> <a target="_blank" href="pyproject.toml" title="Version"><img src="https://img.shields.io/static/v1?label=Version&message=0.1.0&color=red&style=flat-square"></a>
</h1>
The simplest loading bar for python.
<br /><br />
<img src="https://cdn.discordapp.com/attachments/699852562505138236/997716679859650590/lowbar_demo.gif" width="80%">
<details>
<summary><em>demo.py</em></summary>
<div align="left">
<pre>
<code># All the sleep calls would be tasks to
# complete in a real program
<br />
import lowbar, time, random
<br />
bar = lowbar.lowbar()
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
<div align="center">
<a href="INSTALLATION.md">Installation</a> &nbsp; | &nbsp;
<a href="DOCUMENTATION.md">Documentation</a> &nbsp; | &nbsp;
<a href="LICENSE">License</a>
</div>