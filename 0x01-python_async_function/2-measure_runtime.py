#!/usr/bin/env python3

"""The basics of async"""


from asyncio import run
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """masure time of execution"""
    start: float = time()
    run(wait_n(n, max_delay))
    end: float = time()
    TimeVal: float = (end - start) / n
    return TimeVal
