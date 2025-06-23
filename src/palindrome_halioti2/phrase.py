import re

class Phrase:
    """A class to represent phrases."""

    def __init__(self, content):
        self.content = content

    def _processed_content(self):
        """make content lower for palindrome testing"""
        return self.letters_numbers().lower()

    def letters_numbers(self):
        """Return the letters and numbers in the content."""
        return "".join(re.findall("[\\da-zA-Z]",str(self.content)))
    

    def ispalindrome(self):
        """Return whether a string is a palindrome"""
        return self._processed_content() == reverse(self._processed_content())

def reverse(word):
    """reverse a string"""
    return "".join(reversed(word))