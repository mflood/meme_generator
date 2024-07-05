import csv
from typing import List

from quote_engine.ingestor_interface import IngestorInterface, InvalidQuoteLineError
from quote_engine.models import QuoteModel
from utils.logging import logger


class CsvIngestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.lower().endswith(".csv")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:

        logger.debug("%s - extracting quotes from  %s", cls.__name__, path)

        quote_list = []
        with open(path, "r", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                quote = QuoteModel(
                    body=row["body"].strip().strip('"'),
                    author=row["author"].strip(),
                )
                quote_list.append(quote)
        return quote_list


# end
