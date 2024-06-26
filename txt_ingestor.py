
from ingestor_interface import IngestorInterface


class TxtIngestor(IngestorInterface):

    @classmethod    
    def can_ingest(cls, path: str) -> bool:
        return path.lower().endswith(".txt")


if __name__ == "__main__":
    print(TxtIngestor.can_ingest("myfile.txt"))
    print(TxtIngestor.can_ingest("myfile.csv"))
    print(TxtIngestor.can_ingest("myfile.pdf"))
