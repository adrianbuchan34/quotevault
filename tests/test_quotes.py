
def test_random_quote():
    from quotes import random_quote
    assert isinstance(random_quote(), str)
