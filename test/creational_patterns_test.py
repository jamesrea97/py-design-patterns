import unittest

from src.creational_patterns.factory import ModernChairCreator, VictorianChairCreator
from src.creational_patterns.abstract_factory import ModernFurnitureCreator, VictorianFurnitureCreator
from src.creational_patterns.builder import ItalianStylePizzaBuilder, AmericanStylePizzaBuilder
from src.creational_patterns.singleton import DatabaseSingleton


class FactoryMethodShould(unittest.TestCase):
    def test_factory_method(self):
        self.assertEqual(ModernChairCreator(
        ).factory_method().__str__(), "Modern Chair")
        self.assertEqual(VictorianChairCreator(
        ).factory_method().__str__(), "Victorian Chair")


class AbstractFactoryMethodShould(unittest.TestCase):

    def test_abstract_factory_method(self):

        self.assertEqual([f.__str__() for f in ModernFurnitureCreator().factory_method()],
                         ["Modern Chair", "Modern Sofa"])
        self.assertEqual([f.__str__() for f in VictorianFurnitureCreator().factory_method()],
                         ["Victorian Chair", "Victorian Sofa"])


class BuilderShould(unittest.TestCase):

    def test_builder(self):

        self.assertEqual(ItalianStylePizzaBuilder().build(), "Pizza")
        self.assertEqual(AmericanStylePizzaBuilder().build(), "Pizza")

        self.assertEqual(ItalianStylePizzaBuilder().with_cheese().with_meat().build(),
                         "Pizza with toppings: Mozzerella, Prociuto")
        self.assertEqual(AmericanStylePizzaBuilder().with_cheese().with_meat().build(),
                         "Pizza with toppings: Cheddar, Bacon")


class SingletonShould(unittest.TestCase):
    def test_singleton(self):
        data_creator = DatabaseSingleton()

        data_first_call = data_creator.get_instance().get_data()
        data_second_call = data_creator.get_instance().get_data()

        self.assertEqual(data_first_call, data_second_call)
