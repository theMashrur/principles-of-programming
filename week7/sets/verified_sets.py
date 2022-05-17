
class VerifiedSet(set):

    def __init__(self, value):
        for item in value:
            self._verify(item)
        super().__init__(value)

    def _verify(self, value):
        if isinstance(self, VerifiedSet):
            raise NotImplementedError

    def add(self, value):
        self._verify(value)
        super().add(value)

    def update(self, value):
        self._verify(value)
        super().update(value)

    def symmetric_difference_update(self, value):
        self._verify(value)
        super().symmetric_difference_update(value)

    def union(self, other):
        self._verify(other)
        return type(self)(super().union(other))

    def intersection(self, other):
        self._verify(other)
        return type(self)(super().intersection(other))

    def difference(self, other):
        self._verify(other)
        return type(self)(super().difference(other))

    def symmetric_difference(self, other):
        self._verify(other)
        return type(self)(super().symmetric_difference(other))

    def copy(self):
        self._verify(self)
        return type(self)(super().copy())


class IntSet(VerifiedSet):

    def _verify(self, value):
        if not (isinstance(value, int) or isinstance(value, IntSet)):
            raise TypeError(f"IntSet expected an integer, got a {type(value).__name__}") # noqa


class UniquenessError(KeyError):
    pass


class UniqueSet(VerifiedSet):

    def _verify(self, value):
        if value in self:
            raise UniquenessError(f"{value} in set already.")

        elif isinstance(value, set):
            for item in list(value):
                if item in self:
                    raise UniquenessError(f"{value} in set already.")
