from __future__ import annotations

import unicodedata


class AccentNormalizer:
    """
    Removes accent marks.
    """

    def normalize(self, text: str) -> str:
        return "".join(c for c in text if not unicodedata.combining(c))
