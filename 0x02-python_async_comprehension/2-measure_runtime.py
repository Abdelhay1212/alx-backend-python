#!/usr/bin/env python3
''' Run time for four parallel comprehensions '''
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' measure runtime '''
    start_time = time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time()
    runTime = end_time - start_time
    return runTime
