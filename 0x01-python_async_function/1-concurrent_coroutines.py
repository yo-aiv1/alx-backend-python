#!/usr/bin/env python3

"""The basics of async"""


import asyncio
import bisect
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Call and append delay to a list"""
    DelayList: list = []
    for _ in range(n):
        DelayVal: float = await wait_random(max_delay)
        bisect.insort(DelayList, DelayVal)
    return DelayList