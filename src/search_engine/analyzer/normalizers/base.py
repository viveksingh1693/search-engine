from __future__ import annotations

from typing import Protocol


class TextNormalizer(Protocol):
    """
    Contract for all text normalizers.
    """

    def normalize(self, text: str) -> str: ...
