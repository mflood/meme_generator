

from ingestor_interface import IngestorInterface


class PdfIngestor(IngestorInterface):

    @classmethod    
    def can_ingest(cls, path: str) -> bool:
        return path.lower().endswith(".pdf")


if __name__ == "__main__":
    print(PdfIngestor.can_ingest("myfile.txt"))
    print(PdfIngestor.can_ingest("myfile.csv"))
    print(PdfIngestor.can_ingest("myfile.pdf"))

