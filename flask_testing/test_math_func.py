from math_func import add
import pytest

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

@pytest.mark.slow
def test_add_large_numbers():
    assert add(10**6, 10**6) == 2 * 10**6

@pytest.fixture
def sample_data():
    return (3, 5)

def test_add_with_fixture(sample_data):
    a, b = sample_data
    assert add(a, b) == 8

@pytest.mark.parametrize("a,b,result", [(1, 2, 3), (-1, 1, 0), (-1, -1, -2)])
def test_add_parametrized(a, b, result):
    assert add(a, b) == result