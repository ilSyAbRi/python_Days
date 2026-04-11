import sys

if sys.prefix != sys.base_prefix:
    print("Inside virtual environment")
else:
    print("Outside virtual environment")
