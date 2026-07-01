from bank import value

def test_value():
    assert value('Hello') == 0
    assert value('Hashira') == 20
    assert value('Indonesia') == 100
def test_numeric():
    assert value('H4ll0') == 20
    assert value('H4sh1r4') == 20
    assert value('1nd0n3s14') == 100
def test_symbol():
    assert value('He!!@') == 20
    assert value('H@sh!r@') == 20
    assert value('!nd@nes!@') == 100
def test_lower():
    assert value('hello') == 0
    assert value('hashira') == 20
    assert value('indonesia') == 100
def test_upper():
    assert value('HELLO') == 0
    assert value('HASHIRA') == 20
    assert value('INDONESIA') == 100