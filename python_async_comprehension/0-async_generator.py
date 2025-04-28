#!/usr/bin/env python3
import asyncio
import random


async def async_generator():
    """Coroutine qui génère 10 nombres aléatoires entre 0 et 10 avec
    une pause d'1 seconde à chaque fois."""
    for _ in range(10):
        await asyncio.sleep(1)  # Attendre 1 seconde de manière asynchrone
        yield random.uniform(0, 10)  # Générer aléatoire entre 0 et 10
