import re


def remove(text: str) -> str:
    """Method to remove HTML tags from text.

    Args:
        text (str): The text to remove HTML tags from.

    Returns:
        str: The text with removed HTML tags.

    """

    regex = re.compile(r'<.*?>')
    return regex.sub('', text)
