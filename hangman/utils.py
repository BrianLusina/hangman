"""
Utility functions
"""
from typing import Set


def join_guessed_letters(guessed_letters: Set[str]) -> str:
    """
    Joins the guessed letters and returns a string
    Args:
        guessed_letters (set): guessed letters
    Returns:
        str: joined letters as a string separated by a space delimiter
    """
    return " ".join(sorted(guessed_letters))
