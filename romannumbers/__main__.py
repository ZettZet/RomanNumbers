from romannumbers import arabic_to_roman, is_roman, roman_to_arabic


if __name__ == '__main__':
    input_str: str = input('Roman or arabic number: ')

    try:
        out = roman_to_arabic(input_str) if is_roman(
            input_str) else arabic_to_roman(int(input_str))
    except ValueError as ve:
        print(ve)
    else:
        print(out)