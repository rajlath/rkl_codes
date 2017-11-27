from itertools import product

class RangeMinimum(object):
    "Data structure providing efficient range-minimum queries."

    def __init__(self, numbers):
        "Build a RangeMinimum object for the given sequence of numbers."
        # Mapping from (start, step) to min(numbers[start:start + 2**step])
        self._rmq = rmq = {(i, 0): m for i, m in enumerate(numbers)}
        n = len(numbers)
        for step, i in product(range(1, n.bit_length()), range(n)):
            j = i + 2 ** (step-1)
            if j < n:
                rmq[i, step] = min(rmq[i, step-1], rmq[j, step-1])
            else:
                rmq[i, step] = rmq[i, step-1]

    def query(self, start, stop):
        "Return min(numbers[start:stop])."
        j = (stop - start).bit_length() - 1
        x = self._rmq[start, j]
        y = self._rmq[stop - 2 ** j, j]
        return min(x, y)

import unittest
import random

class TestRangeMinimum(unittest.TestCase):
    def test_range_minimum(self):
        n = 1000
        numbers = [random.randrange(n) for _ in range(n)]
        rmq = RangeMinimum(numbers)
        for _ in range(n):
            start, stop = sorted(random.sample(range(n + 1), 2))
            self.assertEqual(rmq.query(start, stop), min(numbers[start:stop]))
