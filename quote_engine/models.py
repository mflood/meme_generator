from dataclasses import dataclass


@dataclass
class QuoteModel:
    """
    Represents a quote
    """

    body: str
    author: str

    def __str__(self):
        return f'"{ self.body }" - {self.author}'

    def __eq__(self, other):
        if isinstance(other, QuoteModel):
            return (
                self.body.lower() == other.body.lower()
                and self.author.lower() == other.author.lower()
            )
        return False

    def __hash__(self):
        return hash((self.body.lower(), self.author.lower()))


if __name__ == "__main__":

    qm = QuoteModel(body="I'm ready", author="Stephen King")
    print(qm)
