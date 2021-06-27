"""Module contains a simple Bridge"""
from abc import ABC, abstractmethod


class AbstractDevice(ABC):

    @abstractmethod
    def set_volume(self, volume: int) -> int:
        pass

    @abstractmethod
    def get_volume(self) -> int:
        pass


class RemoteControl:

    def __init__(self, device: AbstractDevice) -> None:
        self.device = device

    def volume_up(self):
        self.device.set_volume(1)

    def volume_down(self):
        self.device.set_volume(-1)

    def get_control_volume(self) -> int:
        return self.device.get_volume()


class RadioControl(AbstractDevice):
    def __init__(self) -> None:
        self.__volume = 0

    def set_volume(self, volume: int) -> int:
        self.__volume += volume

    def get_volume(self) -> int:
        return self.__volume

# Notes

# When to use
# When you want to divide a class into several variants of some functionalities (e.g. various databases)

# How to implement
# 1. Create AbstractImplementation (AbstractDevice) that all variants implement
# 2. For each variant, create ConcreteImplementation (RadioControl) that implements the functionalities of AbstractImplementation
# 3. Create AbstractionClass (RemoteControl) that is constructed with AbstractImplementation
# 4. At runtime, pass ConcreteImplementation to AbstractionClass to generate specific variant
