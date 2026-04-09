#!/usr/bin/env python3
"""This module defines a function to measure the runtime of async coroutine."""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: float) -> float:
    """Measure the average execution time of wait_n."""

    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    elapsed = total_time / n

    return elapsed
