"""Module contains a simple Builder Design Pattern"""
from typing import Iterator
from abc import ABC, abstractmethod, abstractproperty


class Pizza:
    """
    Base Product class
    Role: Holds state and behaviour to be built-upon
    """

    def __init__(self) -> None:
        self.toppings = []

    def add_topping(self, topping: str) -> None:
        self.toppings.append(topping)

    def __str__(self) -> str:
        str_pizza = "Pizza"
        str_pizza += " with toppings: " + \
            ", ".join(self.toppings) if self.toppings else ""
        return str_pizza


class PizzaBuilder(ABC):
    """
    Abstract Builder class
    Role: creates interface for building Product
    """

    @ abstractmethod
    def build() -> None:
        pass

    @ abstractmethod
    def with_cheese() -> None:
        pass

    @ abstractmethod
    def with_meat() -> None:
        pass


class ItalianStylePizzaBuilder:
    """
    Concrete Builder class
    Role: Builds Product class
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.__pizza = Pizza()

    def build(self) -> None:
        pizza = self.__pizza
        self.reset()
        return pizza.__str__()

    def with_cheese(self) -> None:
        self.__pizza.add_topping("Mozzerella")
        return self

    def with_meat(self) -> None:
        self.__pizza.add_topping("Prociuto")
        return self


class AmericanStylePizzaBuilder:
    """
    Concrete Builder class
    Role: Builds Product class
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.__pizza = Pizza()

    def build(self) -> None:
        pizza = self.__pizza
        self.reset()
        return pizza.__str__()

    def with_cheese(self) -> None:
        self.__pizza.add_topping("Cheddar")
        return self

    def with_meat(self) -> None:
        self.__pizza.add_topping("Bacon")
        return self

# Notes

# Elements
# Product Role: object client would like to interact with
# Creator Role: creates the Product; can handles requests made from client too (see name_furniture())

# When to use
# Want to interact with families (extend Victorian, Modern)
