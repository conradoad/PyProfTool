# PyProfTool

## Overview
Just a little Python-code profiler tool, written only for the purpose of practise coding, packing and publishing on PyPi repository.
It measure the frequency and duration of delimited pieces of code.
## Installing
Run:
```
$ pip3 install PyProfTool
```
## Usage example
### Code:
```python
from pyproftool import PyProfTool
import time

prof = PyProfTool('Profiling Example')
prof.enable()

prof.start_point('All code')

for _ in range(10):
    prof.start_point('Piece of code #1')
    time.sleep(0.1)
    prof.end_point('Piece of code #1')

for _ in range(5):
    prof.start_point('Piece of code #2')
    time.sleep(0.5)
    prof.end_point('Piece of code #2')

prof.end_point('All code')

prof.show()
### Output:

![Screenshot from 2022-08-28 16-06-39](https://user-images.githubusercontent.com/29844580/187091177-af9acbb1-0603-4b90-8872-b0fa39206467.png)
