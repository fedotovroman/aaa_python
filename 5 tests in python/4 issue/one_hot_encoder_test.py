import pytest
from one_hot_encoder import fit_transform

def test_at_least_one_arg():
    """
    checks if an exception is thrown when the method
    is called with no arguments.
    """
    with pytest.raises(TypeError):
        actual = fit_transform()



def main():
    pass

if __name__ == '__main__':
    main()
