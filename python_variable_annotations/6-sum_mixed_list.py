#!/usr/bin/env python3
"""Module that provides a typed function to sum mixed numeric values."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """Return the sum of a list of integers and floating-point numbers."""
    return sum(mxd_lst)
