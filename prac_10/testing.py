"""
CP1404/CP5632 Practical
Testing demo using assert and doctest

"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)
    assert test_car.fuel == 10
    test_car = Car()
    assert test_car.fuel == 0

    test_one_phrase = phrase_as_sentence("hello")
    print(test_one_phrase)

    test_two_phrase = phrase_as_sentence("It is an ex parrot.")
    print(test_two_phrase)

    test_three_phrase = phrase_as_sentence("Capitalise no full stop")
    print(test_three_phrase)


def phrase_as_sentence(phrase):
    final_sentence = phrase.capitalize()
    if final_sentence[-1] != ".":
        final_sentence = final_sentence + "."
    return final_sentence


run_tests()
doctest.testmod()
