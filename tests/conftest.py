from rstr import xeger

from romannumbers import _IS_ROMAN_REGEX


NUM_OF_TESTS = 1000


def generate_random_valid_roman_number() -> str:
    return xeger(_IS_ROMAN_REGEX)
