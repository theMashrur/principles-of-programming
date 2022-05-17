class Fib: # noqa
    """Class for the fibonacci sequence."""

    def __init__(self):
        """Intialise fibonacci sequence."""
        self.val = 1
        self.next = 1

    def __iter__(self):
        """Create iterator protocol."""
        return self

    def __next__(self):
        """Help iterator protocol."""
        self.holder = self.next
        self.val, self.next = self.next, self.val+self.next
        return self.holder

if __name__ == "__main__":
    for n in Fib():
        if n > 100:
            break
        print(n)
