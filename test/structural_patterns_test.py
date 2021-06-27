from abc import abstractmethod
import unittest

from src.structural_patterns.adapter import XML, JSON, InheritanceJSONToXMLAdapter, CompositionJSONToXMLAdapter
from src.structural_patterns.bridge import RemoteControl, RadioControl
from src.structural_patterns.decorator import get_score_implementation


class AdapterSHould(unittest.TestCase):
    def test_adapter_method(self):
        adapter_inheritance = InheritanceJSONToXMLAdapter()

        self.assertTrue(isinstance(adapter_inheritance.process_data(), XML))

        adapter_composition = CompositionJSONToXMLAdapter()

        self.assertTrue(isinstance(adapter_composition.process_data(), XML))


class BridgeSHould(unittest.TestCase):
    def test_adapter_method(self):
        concrete_implemented_radio_control = RadioControl()
        abstracted_remote = RemoteControl(concrete_implemented_radio_control)

        self.assertEqual(abstracted_remote.get_control_volume(), 0)
        abstracted_remote.volume_up()
        self.assertEqual(abstracted_remote.get_control_volume(), 1)
        abstracted_remote.volume_down()
        self.assertEqual(abstracted_remote.get_control_volume(), 0)


class DecoratorShould(unittest.TestCase):
    def test_python_in_built_decorator(self):
        self.assertEqual(get_score_implementation(bonus=10), "Failed")
        self.assertEqual(get_score_implementation(bonus=20), "Passed")
