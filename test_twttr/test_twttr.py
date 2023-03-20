import twttr

def test_uppper():
    assert twttr.shorten("HELLO") == "HLL"
    assert twttr.shorten("WHAT IS YOUR NAME") == "WHT S YR NM"

def test_lower():
    assert twttr.shorten("what is your name?") == "wht s yr nm?"
    assert twttr.shorten("hello") == "hll"