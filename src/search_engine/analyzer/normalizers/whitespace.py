from __future__ import annotations


class WhitespaceNormalizer:
    """
    Removes leading and trailing whitespace.
    """

    def normalize(self, text: str) -> str:
        return text.strip()
