from example_code.groups import Group
import numpy as np


class SymmetricGroup(Group):
    symbol = "S"

    def __init__(self, n):
        super().__init__(n)
        self.check = set([i for i in range(n)])

    def _validate(self, value):
        if not isinstance(value, np.ndarray):
            raise ValueError(f"{value} should be a numpy ndarray")
        elif set(value) != self.check:
            raise ValueError(f"{value} is not a permuation of size {self.n}")

    def operation(self, a, b):
        return a[b]
