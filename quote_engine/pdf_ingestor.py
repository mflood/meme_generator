
from quote_engine.ingestor_interface import IngestorInterface
from quote_engine.models import QuoteModel

import subprocess
import tempfile
import os
from typing import List
import subprocess

def _convert_pdf_to_text(pdf_path: str) -> List[str]:
    with tempfile.TemporaryDirectory() as tmpdirname:
        output_txt_path = os.path.join(tmpdirname, 'output.txt')
        
        try:
            process = subprocess.run(['pdftotext', 
                                      "-raw", 
                                      pdf_path,
                                      output_txt_path], 
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
            
            if process.returncode != 0:
                error_message = process.stderr.decode('utf-8')
                raise Exception(error_message)
            
            lines = []
            with open(output_txt_path, 'r', encoding='utf-8') as file:
                for line in file:
                    lines.append(line.strip())

            return lines
        
        except Exception as error:
            print(f"An exception occurred: {error}")
            raise error

class PdfIngestor(IngestorInterface):

    @classmethod    
    def can_ingest(cls, path: str) -> bool:
        return path.lower().endswith(".pdf")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quote_list = []
        lines = _convert_pdf_to_text(pdf_path=path)
        for row in lines:
            if '-' not in row:
                continue
            body, author = row.rsplit('-', 1)  
            quote = QuoteModel(
                body=body.strip().strip('"'), 
                author=author.strip(),
            )
            quote_list.append(quote)

        return quote_list


if __name__ == "__main__":
    # PYTHONPATH=`pwd` python quote_engine/pdf_ingestor.py 
    print(PdfIngestor.parse(path='_data/DogQuotes/DogQuotesPDF.pdf'))
    print(PdfIngestor.parse(path='_data/SimpleLines/SimpleLines2.pdf'))
    print(PdfIngestor.parse(path='_data/SimpleLines/SimpleLines.pdf'))
