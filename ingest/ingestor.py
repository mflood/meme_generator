
import os

from typing import List
from ingest.models import QuoteModel

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
                print(f"using {ingestor} to parse {path}")
                return ingestor.parse(path)
        
        raise Exception()
        return [] 
 
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
