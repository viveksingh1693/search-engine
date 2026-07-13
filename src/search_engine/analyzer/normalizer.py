from __future__ import annotations

import unicodedata


class Normalizer:
    """Apply common text normalization steps."""

    def normalize(self, text: str) -> str:
        if not text:
            return ""

        normalized = unicodedata.normalize("NFKD", text)
        normalized = "".join(char for char in normalized if not unicodedata.combining(char))
        normalized = normalized.lower().strip()
        return normalized
