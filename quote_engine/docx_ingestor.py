from quote_engine.ingestor_interface import IngestorInterface
from docx import Document
from quote_engine.models import QuoteModel

from typing import List

class DocxIngestor(IngestorInterface):

    @classmethod    
    def can_ingest(cls, path: str) -> bool:
        return path.lower().endswith(".docx")


    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        document = Document(path)

        # Initialize an empty list to hold quote/author pairs
        quotes = []

        # Iterate over each paragraph in the document
        for paragraph in document.paragraphs:
            text = paragraph.text.strip()

            if not text or ' - ' not in text:
                continue
            try:
                # Split only at the last ' - '
                body, author = text.rsplit('-', 1)  
                quote = QuoteModel(
                    body=body.strip().strip('"'),
                    author=author.strip(),
                )
                quotes.append(quote)
            except ValueError:
                print(f"Could not parse: {text}")
        return quotes

if __name__ == "__main__":
    print(DocxIngestor.can_ingest("myfile.txt"))
    print(DocxIngestor.can_ingest("myfile.csv"))
    print(DocxIngestor.can_ingest("myfile.pdf"))

