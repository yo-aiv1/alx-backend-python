#!/usr/bin/env python3

"""The basics of async"""


import asyncio
import time
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """wait for random time"""
    return asyncio.create_task(wait_random(max_delay))
