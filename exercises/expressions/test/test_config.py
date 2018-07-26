import os
import sys

# adding this hack for pytest on Travis-CI
# testing master
sys.path.append(os.getcwd())


def test_config():
    print("configuring tests ...")
