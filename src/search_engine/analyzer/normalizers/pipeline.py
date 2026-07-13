from __future__ import annotations

from search_engine.analyzer.normalizers.base import TextNormalizer


class NormalizationPipeline:
    """
    Executes a chain of text normalizers.
    """

    def __init__(self, normalizers: list[TextNormalizer]):
        self._normalizers = normalizers

    def normalize(self, text: str) -> str:
        for normalizer in self._normalizers:
            text = normalizer.normalize(text)

        return text
