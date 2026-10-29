"""Small, dependency-free text and number helpers."""


def word_count(text):
    """Count whitespace-separated words in *text*."""
    return len(text.split())


def slugify(text):
    """Lowercase a string and join words with single hyphens."""
    words = [w for w in text.lower().split() if w]
    return "-".join(words)


def median(values):
    """Return the median of a non-empty list of numbers.

    For an odd number of samples this is the middle element of the
    sorted list. For an even number of samples the median is the
    average of the two middle elements (issue #1).
    """
    if not values:
        raise ValueError("median() requires at least one value")
    ordered = sorted(values)
    n = len(ordered)
    mid = n // 2
    if n % 2 == 0:
        return (ordered[mid - 1] + ordered[mid]) / 2.0
    return ordered[mid]
