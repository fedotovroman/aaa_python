import pytest
from morse import decode


@pytest.mark.parametrize("test_message, expected",
[('-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.', 'MAI-PYTHON-2019'),
 (' ', ''),
 ('.---- ..--- ...-- .---- ..--- ...-- .---- ..--- ...--', '123123123')])
def test_decode(test_message, expected):
    """
    Checks the decode function against Morse code processing requirements
    """
    assert decode(test_message) == expected

def main():
    pass

if __name__ == '__main__':
    main()
