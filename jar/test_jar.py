from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(8)
    assert jar.size == 8
    with pytest.raises(ValueError):
        jar.deposit(5)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(11)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(2)