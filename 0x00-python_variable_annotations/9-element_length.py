#!/usr/bin/env python3
"""
Type-annotated
return list of tuples with the length of each element function
"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with the length of each element"""
    return [(i, len(i)) for i in lst]
