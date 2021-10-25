import pytest
import sys
import my_module

print(sys.path)


def test_fail():
    mystring = 'This is a string.'
    assert mystring == 'adfsdgs', "This test should fail."


def test_new():
    courses = ['History', 'Math', 'Physics', 'CompSci']
    index = my_module.find_index(courses, 'Math')
    assert index == 1


if __name__ == "__main__":
    pytest.main()
