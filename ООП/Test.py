import pytest
from lesson import *


def test_some_file_creation():
    assert some_file('test.txt', '123') == 'Success'


def test_some_file_open():
    file_name = 'test.txt'
    some_file(file_name, '123')
    text = ''
    with open(file_name, 'r') as f:
        text = f.read()
    assert '123' == text