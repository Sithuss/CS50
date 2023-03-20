from bank import value

def test_0():
    assert value("hello") == 0
    assert value("HeLLo") == 0

def test_20():
    assert value("hai") == 20
    assert value("Hai") == 20
    assert value("hola") == 20
    assert value("hOlA") == 20

def test_100():
    assert value("correct") == 100
    assert value("CoRrEcT") == 100