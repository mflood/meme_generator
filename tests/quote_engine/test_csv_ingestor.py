import csv
from unittest.mock import mock_open, patch

import pytest

from quote_engine.csv_ingestor import CsvIngestor, InvalidCsvFileError
from quote_engine.models import QuoteModel


@pytest.fixture
def mock_csv_file(tmp_path):
    lines = [
        "body,author\n",
        '"Life is beautiful",Anonymous\n',
        '"To be or not to be",Shakespeare\n',
    ]
    path = tmp_path / "test.csv"
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    return path


def test_can_ingest():
    assert CsvIngestor.can_ingest("test.csv") == True
    assert CsvIngestor.can_ingest("test.pdf") == False
    assert CsvIngestor.can_ingest("test.txt") == False
    assert CsvIngestor.can_ingest("test.docx") == False


def test_parse(mock_csv_file):
    quotes = CsvIngestor.parse(mock_csv_file)
    assert len(quotes) == 2
    assert quotes[0].body == "Life is beautiful"
    assert quotes[0].author == "Anonymous"
    assert quotes[1].body == "To be or not to be"
    assert quotes[1].author == "Shakespeare"


def test_parse_invalid_csv():
    mock_csv_content = 'body,author\n"Invalid quote"'
    with patch("builtins.open", mock_open(read_data=mock_csv_content)):
        with pytest.raises(InvalidCsvFileError):
            CsvIngestor.parse("fake_path.csv")


if __name__ == "__main__":
    pytest.main()
