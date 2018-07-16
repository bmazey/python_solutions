import os
import sys

# adding this hack for pytest on Travis-CI
sys.path.append(os.getcwd())


def test_config():
    print("configuring tests ...")
