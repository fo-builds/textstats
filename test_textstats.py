from textstats import median, slugify, word_count


def test_word_count():
    assert word_count("hello world") == 2
    assert word_count("") == 0


def test_slugify():
    assert slugify("Hello World") == "hello-world"
    assert slugify("  multiple   spaces ") == "multiple-spaces"


def test_median_odd():
    assert median([3, 1, 2]) == 2
    assert median([5]) == 5


def test_median_rejects_empty():
    try:
        median([])
        assert False, "expected ValueError"
    except ValueError:
        pass


def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5
    assert median([10, 20]) == 15.0
