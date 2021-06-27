"""Module contains a simple Template Method Design Pattern"""
from abc import ABC, abstractmethod, abstractproperty


class TemplateBuilding(ABC):

    def patrially_construct_house(self) -> str:
        # Processes common to all Buildings
        return "House constructed, walls made of "

    @abstractmethod
    def get_walls_material(self) -> str:
        pass


class GlassBuilding(TemplateBuilding):

    def get_walls_material(self) -> str:
        return "Glass"

    def construct_house(self) -> str:
        # Processes specific to GlassBuilding
        return self.patrially_construct_house() + self.get_walls_material()


class BrickBuilding(TemplateBuilding):

    def get_walls_material(self) -> str:
        return "Brick"

    def construct_house(self) -> str:
        # Processes specific to Brickbuilding
        return self.patrially_construct_house() + self.get_walls_material()

# Notes

# When to use
# Want client to extend only part of the stpes of the algorithm

# How to implement:
# 1. Create an AbstractObject for the common steps
# 2. Create specific ConcreteObjects for non-common steps, implement these, calling AbstractObject if needs be.


# Issues - tight coupling as you cannot have an instance of the BaseClass since abstract.
