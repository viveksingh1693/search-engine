from __future__ import annotations

from typing import Protocol


class TextAnalyzer(Protocol):
    def analyze(self, text: str) -> list[str]: ...
