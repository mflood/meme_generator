

from dataclasses import dataclass

@dataclass
class QuoteModel:
    """
    Represents a quote
    """
    author: str
    body: str
