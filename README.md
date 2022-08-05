<div align="center">
<h1>
lowbar<br />
<a target="_blank" href="pyproject.toml" title="Version"><img src="https://img.shields.io/static/v1?label=Version&message=0.1.3&color=red"></a> <a target="_blank" href="LICENSE" title="License"><img src="https://img.shields.io/static/v1?label=License&message=The%20Unlicense&color=blue"></a> <a target="_blank" href="https://github.com/AnnikaV9/lowbar/actions/workflows/pylint.yml"><img src="https://github.com/AnnikaV9/lowbar/actions/workflows/pylint.yml/badge.svg"></a>
</h1>

The simplest no-nonsense loading bar for python.
<br /><br />
<img src="https://user-images.githubusercontent.com/68383195/179389436-a33af225-ba39-4b3e-bb6c-f0f5f25417f3.gif" width="80%">
<br /><br /><details>
<summary><em>demo.py</em></summary>
<div align="left">
<br /><pre>
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
