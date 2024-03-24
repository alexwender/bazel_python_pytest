from testlib.dummy import dummy_true

import pytest
import sys

def test_dummy_function():
    assert dummy_true() == True

    assert dummy_true() == False


if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))