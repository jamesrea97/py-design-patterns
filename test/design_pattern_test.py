import unittest

from src.abstract_factory import ModernFurnitureCreator, VictorianFurnitureCreator
from src.builder import ItalianStylePizzaBuilder, AmericanStylePizzaBuilder


class AbstractFactoryMethodShould(unittest.TestCase):

    def test_factory_method(self):

        self.assertEqual(ModernFurnitureCreator().name_furniture(),
                         ("Modern Chair", "Modern Sofa"))
        self.assertEqual(VictorianFurnitureCreator().name_furniture(),

                         ("Victorian Chair", "Victorian Sofa"))


class BuilderShould(unittest.TestCase):

    def test_factory_method(self):

        self.assertEqual(ItalianStylePizzaBuilder().build(), "Pizza")
        self.assertEqual(AmericanStylePizzaBuilder().build(), "Pizza")

        self.assertEqual(ItalianStylePizzaBuilder().with_cheese().with_meat().build(),
                         "Pizza with toppings: Mozzerella, Prociuto")
        self.assertEqual(AmericanStylePizzaBuilder().with_cheese().with_meat().build(),
                         "Pizza with toppings: Cheddar, Bacon")
