import pytest
from ciphers.substitution import transform

def test_transform():
    assert transform("ABC") == "ZYX"
    assert transform("abc") == "zyx"
    assert transform("xyz") == "cba"
    assert transform("Hello") == "Svool"
    assert transform("Hello, World! 123") == "Svool, Dliow! 123"
    assert transform("") == ""

    assert transform("Hello! 123", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "QWERTYUIOPASDFGHJKLZXCVBNM") == "Itssg! 123"
    
    text = "Hello, Qu0i's github!"
    assert transform(transform(text)) == text
