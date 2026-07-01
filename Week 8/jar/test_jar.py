from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    with pytest.raises(ValueError):
        Jar(-5)
    with pytest.raises(ValueError):
        Jar("Sepuluh")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(9)
    jar.deposit(9)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar(9)
    jar.deposit(9)
    jar.withdraw(8)
    assert str(jar) == "🍪"
    with pytest.raises(ValueError):
        jar.withdraw(10)