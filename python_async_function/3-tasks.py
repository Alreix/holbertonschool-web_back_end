#!/usr/bin/env python3
"""This module defines a function that creates and returns an asyncio task."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return a task for the wait_random coroutine."""
    task = asyncio.create_task(wait_random(max_delay))
    return task
