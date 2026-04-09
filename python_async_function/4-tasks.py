#!/usr/bin/env python3
"""This module defines a coroutine that runs multiple asyncio tasks."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return the delays ascending order."""
    delays = []

    coroutines = [task_wait_random(max_delay) for i in range(n)]

    for coroutine in asyncio.as_completed(coroutines):
        delay = await coroutine
        delays.append(delay)

    return delays
