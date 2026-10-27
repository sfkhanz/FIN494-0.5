"""Local Python runtime check using only the standard library."""
import sys
from pathlib import Path
simple_return = 102.0 / 100.0 - 1
assert abs(simple_return - 0.02) < 1e-12
print("Python:", sys.version.split()[0])
print("Interpreter:", sys.executable)
print("Working folder:", Path.cwd())
print(f"Python return: {simple_return:.2%}")
print("Checks passed.")
