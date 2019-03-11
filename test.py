import argparse

import pytest

from find_subsequence import find_highest_sum, check_n


@pytest.mark.parametrize('test_file, n, behavior, expected', [
    ('data/input_1.txt', 9, 'values', 6),
    ('data/input_2.txt', 10, 'values', 27),
    ('data/input_3.txt', 30, 'values', 44),
    ('data/input_1.txt', 4, 'differences', 16),
    ('data/input_2.txt', 5, 'differences', 58),
    ('data/input_3.txt', 10, 'differences', 40)
])
def test_highest_sum(test_file, n, behavior, expected):
    assert find_highest_sum(test_file, n, behavior) == expected


def test_check_n_returns_integer_from_string():
    assert check_n('7') == 7


@pytest.mark.parametrize('n_value, re_match', [
    ('0', r'n must be a positive integer.*'),
    ('3.56', r'n must be an integer, not a float.*')
])
def test_check_n_raises_correct_errors_for_wrong_arguments(n_value, re_match):
    with pytest.raises(argparse.ArgumentTypeError, match=re_match):
        check_n(n_value)
