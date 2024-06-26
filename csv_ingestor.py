



from ingestor_interface import IngestorInterface

class CsvIngestor(IngestorInterface):

    @classmethod    
    def can_ingest(cls, path: str) -> bool:
        return path.lower().endswith(".csv")


if __name__ == "__main__":
    print(CsvIngestor.can_ingest("myfile.txt"))
    print(CsvIngestor.can_ingest("myfile.csv"))
    print(CsvIngestor.can_ingest("myfile.pdf"))
    pass
