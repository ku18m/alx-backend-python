#!/usr/bin/env python3
"""Async generator"""
from asyncio import gather
from time import perf_counter


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return the runtime of 4 calls of async_comprehension"""
    start = perf_counter()
    await gather(*[async_comprehension() for _ in range(4)])
    return perf_counter() - start
