class Deque: # noqa
    """Class for deque objects."""

    def __init__(self, n):
        """Construct empty Deque."""
        self.deque = [None] * n
        self.n = n

    def append(self, x):
        """Append objects to deque."""
        if self.deque == [None] * self.n:
            self.deque[0] = x
        elif self.deque[0]:
            for i in range(self.n):
                if isinstance(self.deque[i], type(None)):
                    self.deque[i] = x
                    break
        elif not self.deque[-1]:
            for i in range(self.n):
                if self.deque[-1]:
                    self.deque[-i + 1] = x
                    break
        else:
            for i in range(self.n):
                if not self.deque[-i]:
                    del self.deque[-i]
                    self.deque.append(x)
                    break

    def appendleft(self, x):
        """Add objects to beginning of Deque."""
        if self.deque == [None] * self.n:
            self.deque[0] = x
        elif self.deque[0]:
            self.deque.insert(0, x)
            if len(self.deque) > self.n:
                del self.deque[-1]

    def pop(self):
        """Pop objects from end of deque."""
        if len(self.deque) == 1:
            return self.deque[0]
        for i in range(1, self.n):
            if self.deque[-i] is not None:
                val = self.deque[-i]
                self.deque[-i] = None
                return val

    def popleft(self):
        """Pop objects from start of Deque."""
        for i in range(self.n):
            if self.deque[i] is not None:
                val = self.deque[i]
                self.deque[i] = None
                return val

    def peek(self):
        """See object at the end of the stack."""
        for i in range(1, self.n):
            if self.deque[-i] is not None:
                return self.deque[-i]

    def peekleft(self):
        """See object at the beginning of the stack."""
        for i in range(self.n):
            if self.deque[i] is not None:
                return self.deque[i]

    def __len__(self):
        """Return length of deque."""
        count = 0
        for i, val in enumerate(self.deque):
            if val:
                count += 1
        return count

    def __iter__(self):
        """Allow deques to be iterable."""
        for i, val in enumerate(self.deque):
            if val:
                self.i = i
                break
        return self

    def __next__(self):
        """Help iter protocol."""
        try:
            self.holder = self.deque[self.i]
        except IndexError:
            raise StopIteration
        self.i += 1
        if not self.holder:
            raise StopIteration
        return self.holder
