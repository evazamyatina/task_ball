"""Module that tests main.py."""

import pytest

import main

data_test_degree_correct_cases = (
    ((2, 2.5, 1), 286.48),
    ((5, 2.5, 1, 34), 10.78),
    ((18, 2.89, 123), 218.09),
    ((23, 2.35, 789), 45.14),
)


@pytest.mark.parametrize('args, expected', data_test_degree_correct_cases)
def test_degree_good(args, expected) -> None:
    """Tests correct cases.

    Args:
        args (tuple[float, float, float]): it's a (time, acceleration, start speed).
        expected (float): correct value.
    """
    assert main.degree(*args) == expected


date_test_degree_error_cases = (
    (0, 0, 0)
)


@pytest.mark.xfail(raises=Exception)
def test_degree_error(args):
    """Tests error cases.

    Args:
        args (tuple[float, float, float]): it's a (time, acceleration, start speed).
    """
    main.degree(*args)
