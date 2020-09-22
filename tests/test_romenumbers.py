import pytest

from .conftest import generate_random_valid_roman_number, NUM_OF_TESTS, to_test


@pytest.mark.parametrize("num", [generate_random_valid_roman_number() for _ in range(NUM_OF_TESTS)])
def test_main(num: str):
    assert num == to_test(num)
