from search_engine.analyzer.normalizer import Normalizer


def test_lowercase() -> None:
    n = Normalizer()

    assert n.normalize("HELLO") == "hello"


def test_accents() -> None:
    n = Normalizer()

    assert n.normalize("Café") == "cafe"


def test_trim() -> None:
    n = Normalizer()

    assert n.normalize("  hello  ") == "hello"


def test_resume() -> None:
    n = Normalizer()

    assert n.normalize("Résumé") == "resume"


def test_empty() -> None:
    n = Normalizer()

    assert n.normalize("") == ""
