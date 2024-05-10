#!/usr/bin/env python3

"""The basics of async"""


import asyncio
import bisect
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Call and append delay to a list"""
    DelayList: list = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        DelayVal = await task
        bisect.insort(DelayList, DelayVal)
    return DelayList
