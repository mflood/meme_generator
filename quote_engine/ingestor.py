from pathlib import Path
from typing import List

from quote_engine.csv_ingestor import CsvIngestor
from quote_engine.docx_ingestor import DocxIngestor
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.models import QuoteModel
from quote_engine.pdf_ingestor import PdfIngestor
from quote_engine.txt_ingestor import TxtIngestor


class UnsupportedFileTypeError(ValueError):
    """Exception raised for unsupported file types."""


class Ingestor(IngestorInterface):

    ingestors = [TxtIngestor, CsvIngestor, PdfIngestor, DocxIngestor]

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        for ingestor in Ingestor.ingestors:
            if ingestor.can_ingest(path):
                return True
        return False

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in Ingestor.ingestors:
            if ingestor.can_ingest(path):
                print(f"using {ingestor} to parse {path}")
                return ingestor.parse(path)

        file_type = Path(path).suffix[1:]
        name = Path(path).name
        message = f"Could not parse '{name}'. Unsupported filetype: {file_type}."
        raise UnsupportedFileTypeError(message)

    @classmethod
    def parse_files(cls, path_list: List[str]) -> List[QuoteModel]:
        quotes: List[QuoteModel] = []
        for path in path_list:
            if Ingestor.can_ingest(path):
                file_quotes = Ingestor.parse(path)
                quotes.extend(file_quotes)
        unique_quotes = list(set(quotes))
        return unique_quotes


if __name__ == "__main__":

    print(Ingestor.can_ingest("myfile.txt"))
    print(Ingestor.can_ingest("myfile.docx"))
    print(Ingestor.can_ingest("myfile.pdf"))
    print(Ingestor.can_ingest("myfile.csv"))
    print(Ingestor.can_ingest("myfile.bmp"))
    Ingestor.parse(path="myfile.bmp")
