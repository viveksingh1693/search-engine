from search_engine.analyzer.tokenizer import Tokenizer


def test_simple_sentence() -> None:
    tokenizer = Tokenizer()

    tokens = tokenizer.tokenize("The cat sat on the mat.")

    assert tokens == [
        "The",
        "cat",
        "sat",
        "on",
        "the",
        "mat",
    ]


def test_empty_string() -> None:
    tokenizer = Tokenizer()

    assert tokenizer.tokenize("") == []


def test_multiple_spaces() -> None:
    tokenizer = Tokenizer()

    tokens = tokenizer.tokenize("cat     dog")

    assert tokens == ["cat", "dog"]


def test_numbers() -> None:
    tokenizer = Tokenizer()

    tokens = tokenizer.tokenize("Windows 11 released in 2021")

    assert tokens == [
        "Windows",
        "11",
        "released",
        "in",
        "2021",
    ]
