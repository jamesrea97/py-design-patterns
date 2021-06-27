"""Module contains a simple Factory Design Pattern"""
from abc import ABC, abstractmethod


class Chair:
    """
    Base Product class
    Role: Holds state and behaviour to be extended (e.g. style)
    """

    def __init__(self):
        self.name = "Chair"

    @abstractmethod
    def style(self) -> str:
        pass

    def __str__(self) -> str:
        return " ".join((self.style(), self.name))


class VictorianChair(Chair):
    """
    Sub Product class 
    Role: Extends on Base class state and behaviour
    """

    def style(self) -> str:
        return "Victorian"


class ModernChair(Chair):
    """
    Sub Product class 
    Role: Extends on Base class state and behaviour
    """

    def style(self) -> str:
        return "Modern"


class ChairCreator(ABC):
    """
    AbstractCreator
    Role: Creates interface for creating the families of objects
    """
    @abstractmethod
    def factory_method(self):
        pass

    def name_furniture(self) -> str:
        return self.factory_method()


class VictorianChairCreator(ChairCreator):
    """
    Non-Abstract Creator (Object family)
    Role: Creates specific family of objects
    """

    def factory_method(self) -> tuple:
        return VictorianChair()


class ModernChairCreator(ChairCreator):
    """
    Non-Abstract Creator (Object family)
    Role: extends AbstractCreator
    """

    def factory_method(self) -> tuple:
        return ModernChair()

# Notes

# When to use
# Don't know what exactly Product objects will look like

# How to implement:
# 1. Create AbstractProduct (Chair) that ConcreteProducts (VictorianChair, ModernChair) can implement
# 2. Create AbstractCreator (ChairCreator) that holds abstract factory_method.
# 3. For each Concrete Product, implement ConcreteCreator (VictorianChairCreator, ModernChairCreator) #
# that implements factory_method that returns ConcreteProduct (VictorianChair, ModernChair)
