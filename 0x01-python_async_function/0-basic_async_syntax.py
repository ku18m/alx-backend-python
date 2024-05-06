#!/usr/bin/env python3
"""Asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument,
    and returns a random number between 0 and the integer argument.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
