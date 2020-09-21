# Roman Numbers Converter

Converts Arabic numbers into Roman and vice versa

## All you need is

```python
from romannumbers import *
```

Star contains both function and regular expression string pattern, which match valid Roman numbers

```python
__all__ = [arabic_to_roman, roman_to_arabic, _regex]
```

## Or you can import only needed functions

## Or you can copy \_\_init\_\_.py and call it as main

It will be like

```bash
Roman or arabic number: 345
cccxlv
```

or

```bash
Roman or arabic number: cccxlv
345
```

## Annotations

`roman_to_arabic` returns Roman number **IN LOWER CASE**

`arabic_to_roman` accepts Roman number **IN ANY CASE**
