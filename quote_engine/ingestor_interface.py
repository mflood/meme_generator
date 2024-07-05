from abc import ABC, abstractmethod
from typing import List

from quote_engine.models import QuoteModel
from utils.logging import logger

class InvalidQuoteLineError(ValueError):
    """
    raised when a line of text is not parseable as a QuoteModel
    """


class IngestorInterface(ABC):

    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        pass

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass

    @classmethod
    def _line_to_quote(cls, line) -> QuoteModel:
        """
        Convert a line representing a quote into a QuoteModel

        line:
            "here is a quote" - by anonymous

        Raises:
            ValueError if the line does not include at least one '-'
        """

        if "-" not in line:
            message = "not a valid quote line: '{line}'"
            raise InvalidQuoteLineError(message)

        body, author = line.rsplit("-", 1)
        quote_model = QuoteModel(
            body=body.strip().strip('"'),
            author=author.strip(),
        )
        return quote_model

    @classmethod
    def parse_lines(cls, lines: List[str]) -> List[QuoteModel]:
        """
        Parse a list of lines into a  list of QuoteModels
        """
        quotes = []

        for idx, text in enumerate(lines):
            try:
                quote = IngestorInterface._line_to_quote(line=text)
                quotes.append(quote)
            except InvalidQuoteLineError:
                logger.debug(f"%s skipping line %s", cls.__name__, idx + 1)

        return quotes

# end
