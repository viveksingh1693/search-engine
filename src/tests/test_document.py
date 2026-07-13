from search_engine.models.document import Document


def test_document_creation() -> None:
    doc = Document(id=1, title="Cat", text="The cat sat on the mat.")

    assert doc.id == 1
    assert doc.title == "Cat"
    assert "cat" in doc.text.lower()
