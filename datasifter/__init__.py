from re import match, IGNORECASE
import operator
import requests

LOWER = "<"
GREATER = ">"
GREATER_OR_EQUALS = ">="
LOWER_OR_EQUALS = "<="
EQUALS = "=="
NOT_EQUALS = "!="

ops = {
    LOWER: operator.lt,
    GREATER: operator.gt,
    EQUALS: operator.eq,
    LOWER_OR_EQUALS: operator.le,
    GREATER_OR_EQUALS: operator.ge,
    NOT_EQUALS: operator.ne
}

def is_url(text: str) -> bool:
    """
    Returns true or false depending on whether the specified text is a reference.

    Example:\n
    ```
    if is_url("hello.com"):
        print("Text is url")
    else:
        print("Text isn't url")
    ```
    """
    re_pat = r"^((https?|ftp|file)://)?(www\.)?([-A-Za-z0-9+&@#/%?=~_|!:,.;]*)$"
    url_matches = bool(match(re_pat, text, IGNORECASE))
    return url_matches

def contains(text: str, what_contains: str | dict) -> bool:
    """
    Returns true if the specified text contains the specified values, and false otherwise. The specified values can be passed as a str or dict.
    
    Example with str:\n
    ```
    if contains("I hate not tasty tomatos!", "tomatos"):
        print("Word \"tomatos\" is found in text!")
    else:
        print("Good boy :)")
    ```
    \n
    Example with dict:\n
    ```
    if contains("I love PyPi.org and GitHub!", [".org", "GitHub"]):
        print("Words \".org and GitHub\" is found in text <3")
    else:
        print("Words not found in text")
    ```
    """
    if isinstance(what_contains, str):
        return what_contains in text.lower()
    else:
        for value in what_contains:
            if value.lower() in text.lower():
                return True
        return False

def regexp_matches(text: str, pattern: str, ignore_case: bool = True) -> bool:
    """Returns true if the text matches the regular expression, otherwise False. If "ignore_case" is true, the case is ignored."""
    if not ignore_case:
        return bool(match(pattern, text))
    else:
        return bool(match(pattern, text, IGNORECASE))

def in_range(value: int, minimum: int, maximum: int) -> bool:
    """
    Returns true if the specified number is within the radius of the minimum and maximum, otherwise returns false
    
    Example:\n
    ```
    if in_range(12, 8, 10):
        print("Value in range")
    else:
        print("Value out of range!")
    ```
    """
    return minimum <= value <= maximum

def length(value: str | int, length: int) -> bool:
    """
    Returns true if the text number length is equal to the specified length, otherwise false.

    Example:\n
    ```
    if length("Hello, PyPi!, 10):
        print("Text is equal 10 symbols")
    else:
        print("Text isn't equals 10 symbols")
    ```
    """
    if isinstance(value, int):
        return len(str(value)) == length
    else:
        return len(value) == length
    
def length_is(value: str | int, length: int, condition = GREATER) -> bool:
    """
    Returns true if the length of the text or value matches the condition, otherwise false (Conditions can be: GREATER, LOWER, EQUALS, GREATER_OR_EQUALS, LOWER_OR_EQUALS, or NOT_EQUALS).
    
    Example:\n
    ```
    if length_is("Just veeeeeeeeeeeeeeeeeery big text", 10, GREATER_OR_EQUALS):
        print("Text is greater or equal 10 symbols)
    else:
        print("Text isn't greater or equal 10 symbols)
    ```
    """
    if isinstance(value, int):
        return ops[condition](len(str(value)), length)
    else:
        return ops[condition](len(value), length)

def file_is(file: str, format: str) -> bool:
    """Returns true if the file format is equal to the specified one, the path to the file is specified, the format is specified without a point.
    
    Example:\n
    ```
    if file_is("path/to/file.png", "png"):
        print("File is image (.png)!")
    else:
        print("File isn't image!)
    ```
    """
    return file.endswith(f".{format}")

def is_bad_words(text: str, language_code: str = "eng") -> bool:
    """
    Возвращает true если в указанном тексте есть плохие матные слова, доступные языки: rus, eng

    Example:\n
    ```
    if is_bad_words("PyPi is NOT shit!", "eng"):
        print("Founded bad word!")
    else:
        print("Bad words not found, good boy")
    ```
    """
    if language_code == "rus":
        with open('bw_ru.txt', 'r') as f:
            ban_words = [line.strip() for line in f.readlines()]
        for word in ban_words:
            if word in text.lower():
                return True
        return False
    elif language_code == "eng":
        with open('bw_eng.txt', 'r') as f:
            ban_words = [line.strip() for line in f.readlines()]
        for word in ban_words:
            if word in text.lower():
                return True
        return False
    else:
        print("Error in module DataSifter: Unknown language code, available: \"ru, eng\"")

def is_request(url: str) -> bool:
    """
    Sends a request to the specified URL, if the request is not empty - returns true, otherwise false.

    Example:\n
    ```
    if is_request("url_with_response.com"):
        print("There's an response!")
    else:
        print("No response :(")
    ```
    """
    try:
        res = requests.get(url)
        if res.status_code == 200 and res.content:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False