
import os

from typing import List
from models import QuoteModel

from ingest.ingestor_interface import IngestorInterface
from ingest.txt_ingestor import TxtIngestor
from ingest.csv_ingestor import CsvIngestor
from ingest.pdf_ingestor import PdfIngestor
from ingest.docx_ingestor import DocxIngestor

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
                return ingestor.parse(path)
        
        return [] 
 
if __name__ == "__main__":

    print(Ingestor.can_ingest("myfile.txt"))
    print(Ingestor.can_ingest("myfile.docx"))
    print(Ingestor.can_ingest("myfile.pdf"))
    print(Ingestor.can_ingest("myfile.csv"))
    print(Ingestor.can_ingest("myfile.bmp"))