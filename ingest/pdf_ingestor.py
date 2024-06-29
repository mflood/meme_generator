
from ingest.ingestor_interface import IngestorInterface
from models import QuoteModel

from typing import List


class PdfIngestor(IngestorInterface):

    @classmethod    
    def can_ingest(cls, path: str) -> bool:
        return path.lower().endswith(".pdf")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        return []


if __name__ == "__main__":
    print(PdfIngestor.can_ingest("myfile.txt"))
    print(PdfIngestor.can_ingest("myfile.csv"))
    print(PdfIngestor.can_ingest("myfile.pdf"))

