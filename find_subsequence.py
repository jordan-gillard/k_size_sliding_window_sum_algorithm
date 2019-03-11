import argparse
import pandas as pd
import numpy as np


def find_highest_sum(file_path: str, max_array_size: int, behavior: str) -> int:
    """Finds the highest consecutive sum for n-length sequences in a list of numbers.
    Args:
        file_path (str): The path to the txt file with the numbers sequence.
        max_array_size (int): Max length of the subsequence.
        behavior (str): Either 'values' or 'differences'. Changes how the metric is calculated by determining whether
            this function returns the largest sum of a subsequence or largest sum of a subsequence of absolute
            values of the differences of neighboring pairs.

    Returns:
        highest_sum (int): The sum of the desired non-empty sequence
    """
    all_numbers = pd.read_csv(file_path, sep=' ', header=None, nrows=1).values[0]
    if behavior == 'differences':
        all_numbers = np.ediff1d(all_numbers)
        all_numbers = np.apply_along_axis(np.absolute, 0, all_numbers)
        max_array_size -= 1
    len_all_numbers = len(all_numbers)
    highest_sum = 0

    for array_size in range(1, max_array_size+1):
        highest_sum_so_far = 0
        for i in range(array_size):
            highest_sum_so_far += all_numbers[i]
        for i in range(array_size, len_all_numbers):
            highest_sum_so_far += all_numbers[i] - all_numbers[i - array_size]
            highest_sum = max(highest_sum, highest_sum_so_far)
    return highest_sum


def check_n(value: str) -> int:
    """Checks that the value for n is a positive integer.
    Args:
        value (str): The value for "n" passed to the argument parser.
    Returns:
        value (int): The value for "n" as an integer.
    """
    value_numeric = pd.to_numeric(value)
    if value_numeric <= 0:
        raise argparse.ArgumentTypeError(f'n must be a positive integer. You entered {value}.')
    if value_numeric.dtype == 'float64':
        raise argparse.ArgumentTypeError(f'n must be an integer, not a float. You entered {value}.')
    return value_numeric


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='absolute or relative path to file with one row of space separated values.')
    parser.add_argument('n', type=check_n, help='')
    parser.add_argument('behavior', choices=['values', 'differences'])
    args = parser.parse_args()
    highest_sum = find_highest_sum(args.file_path, args.n, args.behavior)
    print(highest_sum)
