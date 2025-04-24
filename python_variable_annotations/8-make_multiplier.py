#!/usr/bin/env python3
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def fonct_multiplier(x: float) -> float:
        return x * multiplier
    return fonct_multiplier
