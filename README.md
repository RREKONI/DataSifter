# What's new in 0.0.5?
+ Minor code optimization
+ Clearer tooltips with code examples
+ 3 new filters: "file_is(), is_bad_words(), and is_request()"
+ There's a logo

# DataSifter - Add filters to your code

With the DataSifter module, you can use filters for your conditions in your code.

## Without using DataSifter:
```python
import re

text = "Hello Python!"

if bool(re.match(r"^((https?|ftp|file)://)?(www\.)?([-A-Za-z0-9+&@#/%?=~_|!:,.;]*)$", text, re.IGNORECASE)):
    print("Text is link")
else:
    print("Text isn't link")
```

👎 **Why** write long RegExp patterns, if you can:

## Using DataSifter:
```python
import DataSifter as ds

text = "pypi.org"

if ds.is_url(text):
    print("Text is link")
else:
    print("Text isn't link)
```

# All possible filters and what is specified in them:
```python
is_url(
    text: str
) -> bool

contains(
    text: str,
    what_contains: str | dict
) -> bool

regexp_matches(
    text: str,
    pattern: str,
    ignore_case: bool = True
) -> bool

in_range(
    value: int,
    minimum: int,
    maximum: int
) -> bool

length(
    value: str | int,
    length: int
) -> bool

length_is(
    value: str | int,
    length: int,
    condition: str      # Constant from Module
) -> bool

file_is(
    file: str,       # Path to file
    format: str     # Format without point, like "png"
) -> bool

is_bad_words(
    text: str,
    language_code: str = "eng"     # Available: "rus", "eng"
)

is_request(
    url: str
)
```

# Constants
```
1. EQUALS (==)
2. LOWER (<)
3. GREATER (>)
4. LOWER_OR_EQUALS (<=)
5. GREATER_OR_EQUALS (>=)
6. NOT_EQUALS (!=)
```

# Example of work with constants:
```python
import DataSifter as ds

text = "Hello Python!"

if ds.length_is(text, 5, GREATER_OR_EQUALS):
    print("Text greater or equals then 5")
else:
    print("Text lower then 5")
```
