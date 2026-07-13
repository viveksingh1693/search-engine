from __future__ import annotations

from search_engine.analyzer.normalizers.accent import AccentNormalizer
from search_engine.analyzer.normalizers.lowercase import LowerCaseNormalizer
from search_engine.analyzer.normalizers.pipeline import NormalizationPipeline
from search_engine.analyzer.normalizers.unicode import UnicodeNormalizer
from search_engine.analyzer.normalizers.whitespace import WhitespaceNormalizer
from search_engine.analyzer.tokenizer import Tokenizer


class Analyzer:
    """
    Coordinates text analysis.
    """

    def __init__(
        self,
        normalizer: NormalizationPipeline | None = None,
        tokenizer: Tokenizer | None = None,
    ) -> None:
        self._normalizer = normalizer or NormalizationPipeline(
            [
                UnicodeNormalizer(),
                AccentNormalizer(),
                LowerCaseNormalizer(),
                WhitespaceNormalizer(),
            ]
        )
        self._tokenizer = tokenizer or Tokenizer()

    def analyze(self, text: str) -> list[str]:
        normalized = self._normalizer.normalize(text)

        return self._tokenizer.tokenize(normalized)
