from working import convert
import pytest

def test_normal():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_special():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_error():
    with pytest.raises(ValueError):
         convert('09:00 AM - 7:00 PM')
    with pytest.raises(ValueError):
         convert('9:00AM to 7:00PM')
    with pytest.raises(ValueError):
         convert('09:00 AM to 17:00 PM')
    with pytest.raises(ValueError):
         convert('09:60 AM to 07:00 PM')