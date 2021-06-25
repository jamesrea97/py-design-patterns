import unittest

from src import factory

class FactoryMethodShould(unittest.TestCase):

    def test_factory_method(self):

        self.assertEqual(factory.ModernChairCreator().name_furniture(),"Modern Chair")
        self.assertEqual(factory.VictorianChairCreator().name_furniture(),"Victorian Chair")