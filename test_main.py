"""Module that tests main.py."""

import pytest

from main import degree


data_test_degree = (
    ((2, 2.5, 1), 286.48),
    ((5, 2.5, 1, 34), 10.78),
    ((18, 2.89, 123), 218.09),
    ((23, 2.35, 789), 45.14)
)


@pytest.mark.parametrize('args, expected', data_test_degree)
def test_degree_good(args, expected) -> None:
    assert degree(*args) == expected


@pytest.mark.xfail(raises=Exception)
def test_degree_error():
    degree(0, 0, 0)
