"""Handlers for ensuring the mock data passed will work."""

from .exceptions import UnevenColumnError, ArgError


def _check_col_length(datasets):
    """
    Ensures the length of all lists in a list of lists are equal.

    Parameters
    ----------
    datasets: dict[]
        List of datasets to validate.

    Raises
    ------
    UnevenColumnError
        If the columns do not equal each other.
    """
    for dataset in datasets:
        data = dataset['data']
        col_length = len(data[0])
        for row in data:
            if len(row) != col_length:
                raise UnevenColumnError(data)


def _check_arg_consistency(datasets):
    """
    Ensures if arg is specified on one dataset, it is specified on all
    datasets.

    Parameters
    ----------
    datasets: dict[]
        List of dicts containing the datasets.

    Raises
    ------
    ArgError
        If arg is specified on one dataset and not all others.
    """
    specified = False
    for dataset in datasets:
        if dataset.get('arg'):
            specified = True
        if specified and not dataset.get('arg'):
            raise ArgError


def validate(datasets):
    """
    Helper function to apply all validations.

    Parameters
    ----------
    datasets: dict[]
        list of datasets to validate.
    """
    _check_col_length(datasets)
    _check_arg_consistency(datasets)
