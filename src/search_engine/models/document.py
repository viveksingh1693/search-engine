from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Document:
    """
    Represents a single searchable document.
    """

    id: int
    title: str
    text: str
