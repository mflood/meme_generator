from typing import List

from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.models import QuoteModel


class TxtIngestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.lower().endswith(".txt")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:

        quote_list = []
        with open(path, "r", encoding="utf-8") as handle:
            for idx, row in enumerate(handle):
                if "-" not in row:
                    continue
                body, author = row.rsplit("-", 1)
                quote = QuoteModel(
                    body=body.strip().strip('"'),
                    author=author.strip(),
                )
                quote_list.append(quote)

        return quote_list


if __name__ == "__main__":
    print(TxtIngestor.can_ingest("myfile.txt"))
    print(TxtIngestor.can_ingest("myfile.csv"))
    print(TxtIngestor.can_ingest("myfile.pdf"))
