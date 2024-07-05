import pytest
from unittest.mock import patch, mock_open, MagicMock
from quote_engine.pdf_ingestor import PdfIngestor, _convert_pdf_to_text
from quote_engine.models import QuoteModel
from subprocess import CompletedProcess

def test_can_ingest():
    assert PdfIngestor.can_ingest("test.pdf") == True
    assert PdfIngestor.can_ingest("test.txt") == False
    assert PdfIngestor.can_ingest("test.csv") == False
    assert PdfIngestor.can_ingest("test.docx") == False

@patch("quote_engine.pdf_ingestor.subprocess.run")
@patch("quote_engine.pdf_ingestor.open", new_callable=mock_open, read_data='"Life is beautiful" - Anonymous\n"To be or not to be" - Shakespeare\n')
def test_convert_pdf_to_text(mock_open, mock_run):
    mock_run.return_value = CompletedProcess(args=["pdftotext"], returncode=0)
    
    pdf_path = "test.pdf"
    lines = _convert_pdf_to_text(pdf_path)
    
    assert len(lines) == 2
    assert lines[0] == '"Life is beautiful" - Anonymous'
    assert lines[1] == '"To be or not to be" - Shakespeare'

@patch("quote_engine.pdf_ingestor._convert_pdf_to_text", return_value=['"Life is beautiful" - Anonymous', '"To be or not to be" - Shakespeare'])
def test_parse(mock_convert_pdf_to_text):
    pdf_path = "test.pdf"
    quotes = PdfIngestor.parse(pdf_path)
    
    assert len(quotes) == 2
    assert quotes[0].body == "Life is beautiful"
    assert quotes[0].author == "Anonymous"
    assert quotes[1].body == "To be or not to be"
    assert quotes[1].author == "Shakespeare"

@patch("quote_engine.pdf_ingestor.subprocess.run")
@patch("quote_engine.pdf_ingestor.open", new_callable=mock_open, read_data='Invalid quote line\n"Valid quote" - Author\n')
def test_convert_pdf_to_text_with_invalid_lines(mock_open, mock_run):
    mock_run.return_value = CompletedProcess(args=["pdftotext"], returncode=0)
    
    pdf_path = "test.pdf"
    lines = _convert_pdf_to_text(pdf_path)
    
    assert len(lines) == 2
    assert lines[0] == "Invalid quote line"
    assert lines[1] == '"Valid quote" - Author'

@patch("quote_engine.pdf_ingestor._convert_pdf_to_text", return_value=['Invalid quote line', '"Valid quote" - Author'])
def test_parse_with_invalid_lines(mock_convert_pdf_to_text):
    pdf_path = "test.pdf"
    quotes = PdfIngestor.parse(pdf_path)
    
    assert len(quotes) == 1
    assert quotes[0].body == "Valid quote"
    assert quotes[0].author == "Author"

if __name__ == "__main__":
    pytest.main()

