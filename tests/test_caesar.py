import pytest 
from ciphers.caesar import encrypt, decrypt

def test_caesar_encrypt():
    assert encrypt("hello", 3) == "khoor"
    assert encrypt("hello", 27) == "ifmmp"
    assert encrypt("xyz", 3) == "abc"
    assert encrypt("HELLO", 3) == "KHOOR"
    assert encrypt("Hello, W0rld!", 3) == "Khoor, Z0uog!"

def test_caesar_decrypt():
    assert decrypt("khoor", 3) == "hello"
    assert decrypt("ifmmp", 27) == "hello"
    assert decrypt("abc", 3) == "xyz"
    assert decrypt("KHOOR", 3) == "HELLO"
    assert decrypt("Khoor, Z0uog!", 3) == "Hello, W0rld!"
