#!/usr/bin/env python3
"""Type-annotated tuple return function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a tuple contains a string and the square of the given float"""
    def square(n: float) -> float:
        return n * multiplier
    return square
