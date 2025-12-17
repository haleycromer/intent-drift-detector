import math

def drift_score(previous, current):
    return math.sqrt(sum(
        (c - p) ** 2 for p, c in zip(previous, current)
    ))
