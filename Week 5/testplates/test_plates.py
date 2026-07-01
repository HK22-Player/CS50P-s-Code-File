from plates import is_valid

def test_value():
    assert is_valid('Adjust') == True
    assert is_valid('ABC22D') == False
    assert is_valid('A5') == False

def test_length():
    assert is_valid('A') == False
    assert is_valid('AAA199') == True
    assert is_valid('ABCDEFGH') == False

def test_number_location():
    assert is_valid('2ABC34') == False
    assert is_valid('AAA229') == True
    assert is_valid('AA23B') == False

def test_not_zero():
    assert is_valid('CS50') == True
    assert is_valid('NB007') == False
    assert is_valid('MCR990') == True

def test_not_symbol():
    assert is_valid('Surf') == True
    assert is_valid('h3!!0') == False

def test_alphanumeric():
    assert is_valid('PI3.14') == False
    assert is_valid('CS 50') == False
    assert is_valid('CS50') == True