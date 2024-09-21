import re

def format_string(template, **kwargs):
    """
    Format a string using keyword arguments.

    Args:
        template (str): String template with placeholders
        **kwargs: Keyword arguments to replace placeholders

    Returns:
        str: Formatted string
    """
    return template.format(**kwargs)

def extract_pattern(text, pattern):
    """
    Extract the first occurrence of a pattern from a string.

    Args:
        text (str): Input string
        pattern (str): Regular expression pattern

    Returns:
        str: Extracted pattern or None if not found
    """
    match = re.search(pattern, text)
    return match.group(0) if match else None

def truncate_string(text, max_length):
    """
    Truncate a string to a maximum length.

    Args:
        text (str): Input string
        max_length (int): Maximum length

    Returns:
        str: Truncated string
    """
    return text[:max_length]

def strip_whitespace(text):
    """
    Remove leading and trailing whitespace from a string.

    Args:
        text (str): Input string

    Returns:
        str: String with whitespace removed
    """
    return text.strip()
