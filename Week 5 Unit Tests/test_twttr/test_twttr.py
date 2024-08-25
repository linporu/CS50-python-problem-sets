from twttr import shorten
import pytest

def test_default():
    assert shorten("twitter") == "twttr"

def test_case_sensitivity():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("AEIOUaeiou") == ""
    assert shorten("BbCcDd") == "BbCcDd"

def test_non_alpha():
    assert shorten("1234!@#$") == "1234!@#$"
