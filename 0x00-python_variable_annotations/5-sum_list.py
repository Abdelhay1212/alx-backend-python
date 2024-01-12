#!/usr/bin/env python3
'''Complex types - list of floats'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''returns the sum of the list passed as a float'''
    total: float = 0.0

    for num in input_list:
        total += num
    return total
