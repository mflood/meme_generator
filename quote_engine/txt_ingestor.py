from typing import List

from quote_engine.models import QuoteModel
from quote_engine.ingestor_interface import IngestorInterface, InvalidQuoteLineError
from utils.logging import logger


class TxtIngestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.lower().endswith(".txt")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        logger.debug("%s - extracting quotes from  %s", cls.__name__, path)
        with open(path, "r", encoding="utf-8") as handle:
            return IngestorInterface.parse_lines(lines=list(handle))


# end
