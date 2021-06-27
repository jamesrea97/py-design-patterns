"""Module contains a simple Iterator Design Pattern"""
from collections.abc import Iterator


class Doubles(Iterator):
    def __init__(self, elements: list) -> None:
        self.elements = elements
        self.position = 0

    def __next__(self) -> int:

        if self.position >= len(self.elements):
            raise StopIteration
        data = self.elements[self.elements]
        self.position += 2
        return data


# When to use
# Would like to extend the behviour of a collection

# How to implement
# Extend the Python iteration protocol
