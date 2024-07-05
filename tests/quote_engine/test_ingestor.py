import pytest
from pathlib import Path
from quote_engine.ingestor import Ingestor
from quote_engine.models import QuoteModel

@pytest.fixture
def mock_txt_file(tmp_path):
    lines = [
        '"Life is beautiful" - Anonymous\n',
        '"To be or not to be" - Shakespeare\n'
    ]
    path = tmp_path / "test.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    return path

def test_can_ingest(mock_txt_file):
    assert Ingestor.can_ingest(str(mock_txt_file)) == True
    assert Ingestor.can_ingest("test.pdf") == True
    assert Ingestor.can_ingest("test.csv") == True
    assert Ingestor.can_ingest("test.docx") == True
    assert Ingestor.can_ingest("test.bmp") == False

def test_parse(mock_txt_file):
    quotes = Ingestor.parse(str(mock_txt_file))
    assert len(quotes) == 2
    assert quotes[0].body == "Life is beautiful"
    assert quotes[0].author == "Anonymous"
    assert quotes[1].body == "To be or not to be"
    assert quotes[1].author == "Shakespeare"

def test_parse_files(mock_txt_file):
    paths = [str(mock_txt_file)]
    quotes = Ingestor.parse_files(paths)
    assert len(quotes) == 2

    bodies = {quote.body for quote in quotes}
    authors = {quote.author for quote in quotes}

    assert "Life is beautiful" in bodies
    assert "To be or not to be" in bodies
    assert "Anonymous" in authors
    assert "Shakespeare" in authors

if __name__ == "__main__":
    pytest.main()

