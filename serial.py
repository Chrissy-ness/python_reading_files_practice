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
        """Make a generator of numbers with the given value as start""" 
        self.start = self.next = start


    def generate(self):
        self.next += 1
        
        return self.next -1

    def __repr__(self):
        """Show the generated class variable when called."""
        return f"<SerialGenerator start = {self.start} next={self.next}>"
