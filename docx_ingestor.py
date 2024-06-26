from ingestor_interface import IngestorInterface

class DocxIngestor(IngestorInterface):

    @classmethod    
    def can_ingest(cls, path: str) -> bool:
        return path.lower().endswith(".docx")


if __name__ == "__main__":
    print(DocxIngestor.can_ingest("myfile.txt"))
    print(DocxIngestor.can_ingest("myfile.csv"))
    print(DocxIngestor.can_ingest("myfile.pdf"))

