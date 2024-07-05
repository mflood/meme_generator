import pytest

from quote_engine.models import QuoteModel


def test_quote_model_str():
    quote = QuoteModel(body="Life is beautiful", author="Anonymous")
    assert str(quote) == '"Life is beautiful" - Anonymous'


def test_quote_model_equality():
    quote1 = QuoteModel(body="Life is beautiful", author="Anonymous")
    quote2 = QuoteModel(body="Life is beautiful", author="Anonymous")
    quote3 = QuoteModel(body="Life is beautiful", author="Unknown")

    assert quote1 == quote2
    assert quote1 != quote3


def test_quote_model_hash():
    quote1 = QuoteModel(body="Life is beautiful", author="Anonymous")
    quote2 = QuoteModel(body="Life is beautiful", author="Anonymous")

    assert hash(quote1) == hash(quote2)


def test_quote_model_inequality_different_body():
    quote1 = QuoteModel(body="Life is beautiful", author="Anonymous")
    quote2 = QuoteModel(body="Life is hard", author="Anonymous")

    assert quote1 != quote2


def test_quote_model_inequality_different_author():
    quote1 = QuoteModel(body="Life is beautiful", author="Anonymous")
    quote2 = QuoteModel(body="Life is beautiful", author="Unknown")

    assert quote1 != quote2


if __name__ == "__main__":
    pytest.main()
