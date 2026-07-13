from search_engine.analyzer.analyzer import Analyzer


def test_simple_sentence() -> None:
    analyzer = Analyzer()

    tokens = analyzer.analyze("The Cat Sat On The Mat")

    assert tokens == [
        "the",
        "cat",
        "sat",
        "on",
        "the",
        "mat",
    ]


def test_unicode_normalization() -> None:
    analyzer = Analyzer()

    tokens = analyzer.analyze("Café")

    assert tokens == ["cafe"]


def test_trim_whitespace() -> None:
    analyzer = Analyzer()

    tokens = analyzer.analyze("   Hello World   ")

    assert tokens == [
        "hello",
        "world",
    ]


def test_numbers() -> None:
    analyzer = Analyzer()

    tokens = analyzer.analyze("Windows 11")

    assert tokens == [
        "windows",
        "11",
    ]


def test_empty_string() -> None:
    analyzer = Analyzer()

    assert analyzer.analyze("") == []


def test_multiple_spaces() -> None:
    analyzer = Analyzer()

    tokens = analyzer.analyze("cat      dog")

    assert tokens == [
        "cat",
        "dog",
    ]
