from search_engine.analyzer.analyzer import Analyzer
from search_engine.analyzer.normalizers.accent import AccentNormalizer
from search_engine.analyzer.normalizers.lowercase import LowerCaseNormalizer
from search_engine.analyzer.normalizers.unicode import UnicodeNormalizer
from search_engine.analyzer.normalizers.whitespace import WhitespaceNormalizer
from search_engine.analyzer.tokenizer import Tokenizer
from search_engine.common.pipeline import NormalizationPipeline


def create_default_analyzer() -> Analyzer:
    pipeline = NormalizationPipeline(
        [
            UnicodeNormalizer(),
            AccentNormalizer(),
            LowerCaseNormalizer(),
            WhitespaceNormalizer(),
        ]
    )

    tokenizer = Tokenizer()

    return Analyzer(
        normalizer=pipeline,
        tokenizer=tokenizer,
    )
