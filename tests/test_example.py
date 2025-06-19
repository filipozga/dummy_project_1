from example_package_fidev.example import add_one
import pytest

def test_add_one_positive():
    assert add_one(1) == 2
    
def test_add_one_negative():
    assert add_one(-1) == 0
    
def test_add_one_zero():
    assert add_one(0) == 1

def test_add_one_type_error():
    with pytest.raises(TypeError):
        add_one("1")