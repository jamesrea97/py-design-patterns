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


class Sofa:
    """
    Base Product class
    Role: Holds state and behaviour to be extended (e.g. style)
    """

    def __init__(self):
        self.name = "Sofa"

    @abstractmethod
    def style(self) -> str:
        pass

    def __str__(self) -> str:
        return " ".join((self.style(), self.name))


class VictorianSofa(Sofa):
    """
    Sub Product class 
    Role: Extends on Base class state and behaviour
    """

    def style(self) -> str:
        return "Victorian"


class ModernSofa(Sofa):
    """
    Sub Product class 
    Role: Extends on Base class state and behaviour
    """

    def style(self) -> str:
        return "Modern"


class FurnitureCreator(ABC):
    """
    AbstractCreator
    Role: Creates interface for creating the families of objects
    """
    @abstractmethod
    def factory_method(self):
        pass

    def name_furniture(self) -> str:
        return self.factory_method()


class VictorianFurnitureCreator(FurnitureCreator):
    """
    Non-Abstract Creator (Object family)
    Role: Creates specific family of objects
    """

    def factory_method(self) -> tuple:
        return (VictorianChair().__str__(), VictorianSofa().__str__())


class ModernFurnitureCreator(FurnitureCreator):
    """
    Non-Abstract Creator (Object family)
    Role: extends AbstractCreator
    """

    def factory_method(self) -> tuple:
        return (ModernChair().__str__(), ModernSofa().__str__())


# Notes

# When to use
# Want to interact with families (extend Victorian, Modern)

# How to implement:
# 1. Create Abstract Product that Concrete Products can implement
# 2. Create Abstract Creator that holds abstract factory_method.
# 3. For each family, implement Concrete Products and a Concrete Creator that implements factory_method,
# which returns the corresponding family of Products
