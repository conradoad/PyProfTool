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