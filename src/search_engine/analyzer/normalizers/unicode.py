from __future__ import annotations

import unicodedata


class UnicodeNormalizer:
    """
    Converts Unicode into canonical form.
    """

    def normalize(self, text: str) -> str:
        return unicodedata.normalize("NFKD", text)
