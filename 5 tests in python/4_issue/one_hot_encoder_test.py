import pytest
from one_hot_encoder import fit_transform


def test_all_features_are_different():
    """
    checks if the method works correctly if all arguments are different.
    """
    actual = fit_transform(['Alpha', 'Beta', 'Gamma', 'Delta'])
    expected = [('Alpha', [0, 0, 0, 1]),
                ('Beta', [0, 0, 1, 0]),
                ('Gamma', [0, 1, 0, 0]),
                ('Delta', [1, 0, 0, 0])]
    assert actual == expected

def test_some_features_are_equal():
    """
    checks if the method works correctly if there are identical arguments.
    """
    actual = fit_transform(['Alpha', 'Alpha', 'Alpha', 'Delta'])
    expected = [('Alpha', [0, 1]),
                ('Alpha', [0, 1]),
                ('Alpha', [0, 1]),
                ('Delta', [1, 0])]
    assert actual == expected

def test_ft_returns_list():
    """
    checks if the method returns a list object.
    """
    actual = fit_transform(['Alpha', 'Beta', 'Gamma'])
    assert isinstance(actual, list)

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
