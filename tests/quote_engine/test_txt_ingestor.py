from unittest.mock import mock_open, patch

import pytest

from quote_engine.models import QuoteModel
from quote_engine.txt_ingestor import TxtIngestor


@pytest.fixture
def mock_txt_file(tmp_path):
    lines = [
        '"Life is beautiful" - Anonymous\n',
        '"To be or not to be" - Shakespeare\n',
    ]
    path = tmp_path / "test.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    return path


def test_can_ingest():
    assert TxtIngestor.can_ingest("test.txt") == True
    assert TxtIngestor.can_ingest("test.pdf") == False
    assert TxtIngestor.can_ingest("test.csv") == False
    assert TxtIngestor.can_ingest("test.docx") == False


def test_parse(mock_txt_file):
    quotes = TxtIngestor.parse(mock_txt_file)
    assert len(quotes) == 2
    assert quotes[0].body == "Life is beautiful"
    assert quotes[0].author == "Anonymous"
    assert quotes[1].body == "To be or not to be"
    assert quotes[1].author == "Shakespeare"


def test_parse_invalid_lines():
    mock_txt_content = 'Invalid quote line\n"Valid quote" - Author\n'
    with patch("builtins.open", mock_open(read_data=mock_txt_content)):
        quotes = TxtIngestor.parse("fake_path.txt")
        assert len(quotes) == 1
        assert quotes[0].body == "Valid quote"
        assert quotes[0].author == "Author"


if __name__ == "__main__":
    pytest.main()
