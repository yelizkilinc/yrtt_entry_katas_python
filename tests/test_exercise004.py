# Move the first letter of each word to the end of it, then add "ay" 
# to the end of the word. Leave punctuation marks untouched.
import pytest

from tasks.exercise004 import pig_it

def test_pig_latin_returns_string():
    assert pig_it("Pig latin is cool") == "igPay atinlay siay oolcay"
    assert pig_it("This is my string") == "hisTay siay ymay tringsay"

def test_pig_latin_punctuation():
    assert pig_it("Pig latin is cool!!") == "igPay atinlay siay oolcay!!"