import pytest
from fuel import convert,gauge

def test_convert():
    assert convert('1/2') == 50
    assert convert('3/5') == 60
    assert convert('9/10') == 90

def test_convert_round():
    assert convert('2/3') == 67
    assert convert('1/6') == 17

def test_convert_error():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('4/3')
    with pytest.raises(ValueError):
        convert('cat/dog')
    with pytest.raises(ValueError):
        convert('-1/2')
    with pytest.raises(ValueError):
        convert('-3/5')

def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(67) == '67%'
    assert gauge(20) == '20%'