from __future__ import annotations


class LowerCaseNormalizer:
    """
    Converts text to lowercase.
    """

    def normalize(self, text: str) -> str:
        return text.lower()
