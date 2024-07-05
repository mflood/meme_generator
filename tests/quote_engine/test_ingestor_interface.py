import pytest

from quote_engine.ingestor_interface import IngestorInterface, InvalidQuoteLineError
from quote_engine.models import QuoteModel


def test_line_to_quote_valid():
    line = '"Life is beautiful" - Anonymous'
    quote = IngestorInterface._line_to_quote(line)
    assert quote.body == "Life is beautiful"
    assert quote.author == "Anonymous"


def test_line_to_quote_invalid():
    line = "Life is beautiful Anonymous"
    with pytest.raises(InvalidQuoteLineError):
        IngestorInterface._line_to_quote(line)


def test_parse_lines_valid():
    lines = ['"Life is beautiful" - Anonymous', '"To be or not to be" - Shakespeare']
    quotes = IngestorInterface.parse_lines(lines)
    assert len(quotes) == 2
    assert quotes[0].body == "Life is beautiful"
    assert quotes[0].author == "Anonymous"
    assert quotes[1].body == "To be or not to be"
    assert quotes[1].author == "Shakespeare"


def test_parse_lines_invalid():
    lines = ['"Life is beautiful" - Anonymous', "This is not a valid quote"]
    quotes = IngestorInterface.parse_lines(lines)
    assert len(quotes) == 1
    assert quotes[0].body == "Life is beautiful"
    assert quotes[0].author == "Anonymous"


if __name__ == "__main__":
    pytest.main()
