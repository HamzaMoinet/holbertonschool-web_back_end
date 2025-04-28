import asyncio
from 0-async_generator import async_generator
import random
async def async_comprehension():
    await asyncio.sleep(0)
    return[i async for i in async_generator(random)10]
