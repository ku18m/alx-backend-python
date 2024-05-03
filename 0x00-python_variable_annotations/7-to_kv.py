#!/usr/bin/env python3
"""Type-annotated tuple return function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple contains a string and the square of the given float"""
    return (k, v * v)
