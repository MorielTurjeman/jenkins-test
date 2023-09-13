
import pytest
from add import add

def test_add():
    result = add(2, 2)
    assert result == 4


if __name__ == "__main__": 
    import pytest 
    pytest.main()