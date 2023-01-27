
import allure
import pytest

@pytest.mark.smoke
def test_addition():
    assert 2 + 2 == 4

@pytest.mark.regression
def test_subtraction():
    assert 5 - 2 == 3

@pytest.mark.smoke
def test_multiplication():
    assert 2 * 2 == 4

@pytest.mark.smoke
def test_division():
    assert 8 / 2 == 4
