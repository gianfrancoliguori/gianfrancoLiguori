import pytest 
from functions import *

#1
@pytest.mark.parametrize("dni, expected", [("1234567", True), ("12345678", True), ("123456", False), ("123456789", False)])
def test_document(dni, expected):
    result = document(dni)
    assert result == expected

#2
@pytest.mark.parametrize("input_string, expected_length", [
    ("Hello world", 5),  # La última palabra es "world" con longitud 5
    ("  Python  ", 6),   # La última palabra es "Python" con longitud 6
    ("", 0),             # Cadena vacía, se espera longitud 0
    ("One", 3),          # Una sola palabra "One" con longitud 3
    ("Spaces   ", 6)     # La última palabra es "Spaces" con longitud 6
])
def test_word_len(input_string, expected_length):
    result = word_len(input_string)
    assert result == expected_length

#3
@pytest.mark.parametrize("dni, expected", [("1234567", True), ("12345678", True), ("123456", False), ("123456789", False), ("abcdefg", False)])
def test_validate_dni(dni, expected):
    assert validate_dni(dni) == expected

@pytest.mark.parametrize("name, surname, dni, expected", [
    ("John Doe", "Smith", "1234567", "John7Doe123"),
    ("Alice", "Johnson", "98765432", "Alice8John987"),
    ("Bob", "Brown", "87654321", "Bob5Bro876")
])
def test_generate_identifier(name, surname, dni, expected):
    assert generate_identifier(name, surname, dni) == expected

#4
@pytest.mark.parametrize("num1, num2, expected", [
    (10, 2, True),    
    (15, 3, True),    
    (7, 4, False),    
    (20, 6, False),   
    (8, 0, False)     
])
def test_multiple(num1, num2, expected):
    result = multiple(num1, num2)
    assert result == expected

