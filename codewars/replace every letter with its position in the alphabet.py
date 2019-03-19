In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
soln:
from string import ascii_lowercase
LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}
def alphabet_position(text):
    text = text.lower()
    numbers = [LETTERS[character] for character in text if character in LETTERS]
    return ' '.join(numbers)

from string import ascii_lowercase
cap_letter = {small_letter: str(index) for index, small_letter in enumerate(ascii_lowercase, start=1)}
def alphabet_position(text):
    text = text.lower()
    nos = [cap_letter [char] for char in text if char in cap_letter ]
    return ' '.join(nos)

other coders soln:
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
or 
def alphabet_position(s):
  return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())
or 
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')
or
from string import ascii_lowercase


def alphabet_position(text):
    return ' '.join(str(ascii_lowercase.index(n.lower()) + 1) for n in text if n.isalpha())
or
import re

def alphabet_position(text):
    return " ".join([str(ord(i) - 96) for i in re.findall('[a-z]', text.lower())])