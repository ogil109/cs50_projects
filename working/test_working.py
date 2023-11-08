import pytest
from working import convert

def test_convert_input():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


def test_convert_simple():
    assert convert("8 AM to 2 PM") == '08:00 to 14:00'
    assert convert("10 PM to 05 AM") == '22:00 to 05:00'

def test_convert_complex():
    assert convert("8:35 AM to 2:30 PM") == '08:35 to 14:30'
    assert convert("10:15 PM to 05 AM") == '22:15 to 05:00'