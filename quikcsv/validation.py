"""Handlers for ensuring the mock data passed will work."""

from .exceptions import UnevenColumnError


def _check_col_length(data):
    """
    Ensures the length of all lists in a list of lists are equal.

    Parameters
    ----------
    data: [][]
        List of lists of elements.

    Raises
    ------
    UnevenColumnError
        If the columns do not equal each other.
    """
    col_length = len(data[0])
    for row in data:
        if len(row) != col_length:
            raise UnevenColumnError(data)


def validate(data):
    """
    Helper function to apply all validations.

    Parameters
    ----------
    data: [][]
        The data to validate.
    """
    _check_col_length(data)
