from dataclasses import dataclass


@dataclass(slots=True)
class TermStatistics:
    """
    Collection-wide statistics for a term.
    """

    document_frequency: int = 0
    collection_frequency: int = 0
