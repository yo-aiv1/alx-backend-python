#!/usr/bin/env python3

"""The basics of async"""


import asyncio
import random


async def wait_random(max_delay=10):
    """
    Sleep for random delay from 0 to max delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
