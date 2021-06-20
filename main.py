import os

os.system('kernprof -l snake3')
os.system('python -m line_profiler snake3.lprof')
