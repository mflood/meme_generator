import os
import subprocess
import tempfile
from typing import List

from quote_engine.ingestor_interface import IngestorInterface, InvalidQuoteLineError
from quote_engine.models import QuoteModel
from utils.logging import logger


def _convert_pdf_to_text(pdf_path: str) -> List[str]:
    with tempfile.TemporaryDirectory() as tmpdirname:
        output_txt_path = os.path.join(tmpdirname, "output.txt")

        try:
            process = subprocess.run(
                ["pdftotext", "-raw", pdf_path, output_txt_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            if process.returncode != 0:
                error_message = process.stderr.decode("utf-8")
                raise Exception(error_message)

            lines = []
            with open(output_txt_path, "r", encoding="utf-8") as file:
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
        """
        Concrete implementation of IngestorInterface method

        Params:
            path: the path to the pdf file

        Returns
            list of QuoteModel extracted from the file
        """
        logger.debug("%s - extracting quotes from  %s", cls.__name__, path)
        lines = _convert_pdf_to_text(pdf_path=path)
        return IngestorInterface.parse_lines(lines=lines)

# end
