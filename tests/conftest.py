from rstr import xeger

from romannumbers import _IS_ROMAN_REGEX, arabic_to_roman, roman_to_arabic


NUM_OF_TESTS = 1000

def to_test(roman: str) -> str:
    converted_roman: int = roman_to_arabic(roman)
    converted_arabic: str = arabic_to_roman(converted_roman)

    return converted_arabic


def generate_random_valid_roman_number() -> str:
    return xeger(_IS_ROMAN_REGEX)
