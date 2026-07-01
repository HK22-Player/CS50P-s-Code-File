from seasons import get_birth
import pytest

def test():
    assert get_birth("2025-06-18") == "Five hundred twenty-five thousand, six hundred minutes"
    assert get_birth("2024-06-18") == "One million, fifty-one thousand, two hundred minutes"

def test_format():
    with pytest.raises(ValueError):
        get_birth("January 1, 1999")
    with pytest.raises(ValueError):
        get_birth("01-01-1999")
    with pytest.raises(ValueError):
        get_birth("1999/01/01")
    with pytest.raises(ValueError):
        get_birth("2025-02-30")
    with pytest.raises(ValueError):
        get_birth("2025-13-01")