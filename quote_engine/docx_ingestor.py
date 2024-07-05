from typing import List

from docx import Document

from quote_engine.ingestor_interface import IngestorInterface, InvalidQuoteLineError
from quote_engine.models import QuoteModel
from utils.logging import logger


class DocxIngestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.lower().endswith(".docx")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        logger.debug("%s - extracting quotes from  %s", cls.__name__, path)
        document = Document(path)
        lines = [paragraph.text for paragraph in document.paragraphs]
        return IngestorInterface.parse_lines(lines=lines)

# end
