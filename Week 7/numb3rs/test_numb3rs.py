from numb3rs import validate

def test_numb3rs():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
def test_numb3rs_invalid_range():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("192.168.001.1") == False
def test_numb3rs_invalid_format():
    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False