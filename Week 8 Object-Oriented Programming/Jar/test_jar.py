from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12
    with pytest.raises(ValueError):
        jar.capacity = -1


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises(ValueError):
        jar.deposit("cat")
    jar.deposit(1)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.deposit(12)


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(-1)
    with pytest.raises(ValueError):
        jar.withdraw("cat")
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1
    jar.withdraw(1)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)
