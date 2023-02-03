"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Make generator and start at start"""
        self.start = self.next = start

    def __repr__(self):
        """showing representation"""
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Return the next coming serial"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset number back to original start number"""
        self.next = self.start


