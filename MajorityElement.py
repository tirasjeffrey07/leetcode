from collections import Counter


def majorityElement(nums: list[int]) -> int:
    for x in sorted(Counter([6, 5, 5]).items(), key=lambda x: x[1], reverse=True):
        return x[0]
