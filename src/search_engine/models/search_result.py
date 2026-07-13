from dataclasses import dataclass

from search_engine.models.document import Document


@dataclass(slots=True)
class SearchResult:
    document: Document
    score: float
