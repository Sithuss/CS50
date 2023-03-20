from jar import Jar


def test_init():
    jar = Jar()
    jar.capacity = 14
    assert str(jar) == ""
    jar.capacity = -2 == ValueError("Capacity Error")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"



def test_deposit():
    jar = Jar()
    jar.deposit = 13 == ValueError("Jar exceeded limited amount")


def test_withdraw():
    jar = Jar()
    assert str(jar) == ""
    jar.withdraw = 1 == ValueError("amount exceeded")