from __future__ import annotations

from search_engine.analyzer.normalizers.accent import AccentNormalizer
from search_engine.analyzer.normalizers.lowercase import LowerCaseNormalizer
from search_engine.analyzer.normalizers.unicode import UnicodeNormalizer
from search_engine.analyzer.normalizers.whitespace import WhitespaceNormalizer
from search_engine.analyzer.token_filters.pipeline import TokenFilterPipeline
from search_engine.analyzer.tokenizer import Tokenizer
from search_engine.common.pipeline import NormalizationPipeline
from search_engine.models.token import Token


class Analyzer:
    """
    Coordinates text analysis.
    """

    def __init__(
        self,
        normalizer: NormalizationPipeline | None = None,
        tokenizer: Tokenizer | None = None,
        token_filters: TokenFilterPipeline | None = None,
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
        self._token_filters = token_filters or TokenFilterPipeline([])

    def analyze(self, text: str) -> list[Token]:
        normalized = self._normalizer.normalize(text)

        tokens = self._tokenizer.tokenize(normalized)
        return self._token_filters.apply(tokens)
