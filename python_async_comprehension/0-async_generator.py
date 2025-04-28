#!/usr/bin/env python3
"""
Générateur asynchrone produisant 10 nombres flottants aléatoires entre 0 et 10,
attendant 1 seconde avant chaque valeur produite.
"""
import asyncio
import random


async def async_generator():
    """
    Génère de manière asynchrone 10 nombres flottants aléatoires entre 0 et 10,
    en attendant 1 seconde avant de produire chaque valeur.

    Yields :
        float : Nombre aléatoire entre 0 et 10.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
