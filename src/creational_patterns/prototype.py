"""Module contains a simple Prototype Design Pattern"""
import copy
from typing_extensions import NotRequired


class SomeComponent:

    def __init__(self, some_part: int) -> None:
        self.some_part = some_part

    def __copy__(self):
        """
        Implementationf of shallow copy for SomeComponent
        """
        some_part_shallow_copy = copy.copy(self.some_part)
        new = self.__class__(some_part_shallow_copy)

        new.__dict__.update(self.__dict__)
        return new

    def __deecopy__(self, memo={}):
        """
        Implementation of deep copy for SomeComponent
        memo is used by copy library to prevent infinite recursive copies.
        memo must be passed to all deepcopy.
        """
        some_part_deep_copy = copy.deepcopy(self.some_part, memo=memo)
        new = self.__class__(some_part_deep_copy)

        new.__dict__ = copy.deepcopy(self.__dict__, memo=memo)

        return new


# TODO complete implementation
