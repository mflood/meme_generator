
import csv
from ingest.ingestor_interface import IngestorInterface
from models import QuoteModel

from typing import List


class CsvIngestor(IngestorInterface):

    @classmethod    
    def can_ingest(cls, path: str) -> bool:
        return path.lower().endswith(".csv")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quote_list = []
        with open(path, "r", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                quote = QuoteModel(
                    body=row['body'],
                    author=row['author'],
                )
                quote_list.append(quote)
        return quote_list

# end
