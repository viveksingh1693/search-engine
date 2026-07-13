from dataclasses import dataclass, field


@dataclass(slots=True)
class Posting:
    """
    Represents one document inside a posting list.
    """

    document_id: int
    term_frequency: int = 0
    positions: list[int] = field(default_factory=list)
