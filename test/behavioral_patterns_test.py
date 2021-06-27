from abc import abstractmethod
import unittest

from src.behavioral_patterns.template import GlassBuilding, BrickBuilding
from src.behavioral_patterns.command import LongTaskA, LongTaskB, Executer


class TemplateMethodShould(unittest.TestCase):
    def test_template_method(self):
        pass


class CommandShould(unittest.TestCase):
    def test_command(self):
        executer = Executer()
        self.assertEqual(executer.execute(LongTaskA()),
                         "LongTaskA Step 1 Completed,LongTaskA Step 2 Completed")
        self.assertEqual(executer.execute(LongTaskB()),
                         "LongTaskB Step 1 Completed,LongTaskB Step 2 Completed")
