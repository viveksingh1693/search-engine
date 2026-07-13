from __future__ import annotations

import re


class Tokenizer:
    """
    Splits text into tokens.

    This tokenizer only extracts words.
    It does not lowercase, stem, or remove stop words.
    """

    _TOKEN_PATTERN = re.compile(r"\b\w+\b", re.UNICODE)

    def tokenize(self, text: str) -> list[str]:
        if not text:
            return []

        return self._TOKEN_PATTERN.findall(text)
