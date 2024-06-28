
from ingestor_interface import IngestorInterface
from models import QuoteModel

from typing import List


from ingestor_interface import IngestorInterface


class TxtIngestor(IngestorInterface):

    @classmethod    
    def can_ingest(cls, path: str) -> bool:
        return path.lower().endswith(".txt")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        return []


if __name__ == "__main__":
    print(TxtIngestor.can_ingest("myfile.txt"))
    print(TxtIngestor.can_ingest("myfile.csv"))
    print(TxtIngestor.can_ingest("myfile.pdf"))
