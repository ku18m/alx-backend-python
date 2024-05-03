#!/usr/bin/env python3
"""Type-annotated return first element of a list or None function"""
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a list or None"""
    if lst:
        return lst[0]
    else:
        return None
