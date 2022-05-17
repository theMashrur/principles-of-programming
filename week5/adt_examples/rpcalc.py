from math import sin, cos # noqa
from numbers import Number # noqa

class RPCalc: # noqa
    """Class for Reverse Polish calculator implementation."""

    def __init__(self):
        """Intiialise stack for calculator."""
        self.stack = []

    def push(self, n):
        """Push operators or operands onto stack."""
        if isinstance(n, Number):
            self.stack.append(n)
        elif n == "+":
            num1 = self.stack.pop()
            num2 = self.stack.pop()
            self.stack.append(num1+num2)
        elif n == "-":
            num1 = self.stack.pop()
            num2 = self.stack.pop()
            self.stack.append(num2-num1)
        elif n == "*":
            num1 = self.stack.pop()
            num2 = self.stack.pop()
            self.stack.append(num1*num2)
        elif n == "/":
            num1 = self.stack.pop()
            num2 = self.stack.pop()
            self.stack.append(num2/num1)
        elif n == "sin":
            num = self.stack.pop()
            self.stack.append(sin(num))
        elif n == "cos":
            num = self.stack.pop()
            self.stack.append(cos(num))
        else:
            return NotImplemented

    def pop(self):
        """Pop last item on stack."""
        return self.stack.pop()

    def peek(self):
        """See without popping last item on stack."""
        return self.stack[-1]

    def __len__(self):
        """Return the length of the stack."""
        return len(self.stack)
