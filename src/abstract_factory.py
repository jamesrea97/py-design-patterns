"""Module contains a simple Abstarct Factory Design Pattern"""
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


class FurnitureCreator(ABC):
    """
    Base 
    """
    @abstractmethod
    def factory_method(self):
        pass

    def name_furniture(self) -> str:
        return str(self.factory_method())


class VictorianChairCreator(FurnitureCreator):

    def factory_method(self) -> Chair:
        return VictorianChair()

class ModernChairCreator(FurnitureCreator):

    def factory_method(self) -> Chair:
        return ModernChair()


# Notes

## Elements
# Product Role: object client would like to interact with
# Creator Role: creates the Product; can handles requests made from client too (see name_furniture())


## When to use
# Want to separate Product from Creator (e.g. when you don't know much about the product initially)
