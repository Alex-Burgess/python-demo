import pytest


def test_fail():
    mystring = 'This is a string.'

    # assert mystring == 'adfsdgs', "This test should fail."
    assert False


if __name__ == "__main__":
    pytest.main()
