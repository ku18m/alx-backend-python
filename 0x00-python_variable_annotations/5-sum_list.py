#!/usr/bin/env python3
"""Type-annotated sum_list function"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """Returns the sum of a list of floats"""
    return sum(input_list)
