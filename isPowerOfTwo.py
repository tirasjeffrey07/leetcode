import math


def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    return math.log2(n).is_integer()
