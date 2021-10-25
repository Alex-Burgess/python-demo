import pytest
import sys
import my_module
import requests_mock

print(sys.path)


@pytest.mark.skip(reason="This function could not be test properly.")
def test_fail():
    mystring = 'This is a string.'
    assert mystring == 'adfsdgs', "This test should fail."


def test_new():
    courses = ['History', 'Math', 'Physics', 'CompSci']
    index = my_module.find_index(courses, 'Math')
    assert index == 1


def test_new_2():
    courses = ['History', 'Math', 'Physics', 'CompSci']
    index = my_module.find_index(courses, 'Math')
    assert index == 1


@pytest.mark.skip(reason="This function could not be test properly.")
def test_skip_me():
    courses = ['History', 'Math', 'Physics', 'CompSci']
    index = my_module.find_index(courses, 'Math')
    assert index == 1


class TestApi:
    def test_api_response(self, api_event):
        method = my_module.get_api_method(api_event)
        assert method == 'GET', "Response was not as expected"


class TestExceptions:
    def test_error_function(self):
        with pytest.raises(Exception) as e:
            my_module.error_function(True)
        assert str(e.value) == "An error occurred!"


class TestFoodApi:
    def test_api_without_mock(self):
        establishments = my_module.get_establishment_ratings(1)
        assert len(establishments) == 1488, "Number of establishments was not as expected."

    def test_api_with_mock(self, requests_mock, food_api_response):
        requests_mock.get('http://api.ratings.food.gov.uk/Establishments', json=food_api_response)

        establishments = my_module.get_establishment_ratings(1)
        assert len(establishments) == 1, "Number of establishments was not as expected."


if __name__ == "__main__":
    pytest.main()
