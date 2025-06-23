from pytest import skip
from palindrome_halioti2.phrase import Phrase

def test_non_palindrome():
    assert not Phrase("apple").ispalindrome()
def test_is_palindrome():
    assert Phrase("racecar").ispalindrome()
def test_mixed_case_palindrome():
    assert Phrase("RaCeCar").ispalindrome()
def test_palindrome_with_punctuation():
    assert Phrase("Madam, I'm Adam.").ispalindrome()
def test_letters():
    assert Phrase("Madam, I'm Adam.").letters_numbers() == "MadamImAdam"
def test_palindrome_interger():
    assert Phrase("12321").ispalindrome()
def test_palindrome_non_interger():
    assert not Phrase("5321").ispalindrome()