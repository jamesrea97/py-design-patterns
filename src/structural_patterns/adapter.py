"""Module contains a simple Adapter"""
from abc import ABC, abstractmethod


class XML:
    """Contains XML Example"""


class JSON:
    """Contains JSON Example"""


class AbstractClientXMLParser(ABC):
    @abstractmethod
    def process_data(self) -> XML:
        pass


class ServiceJSON:
    def get_data(self) -> JSON:
        return JSON()


class CompositionJSONToXMLAdapter(AbstractClientXMLParser):
    def __init__(self) -> None:
        self.client_json = ServiceJSON()

    def process_data(self) -> XML:
        data = self.client_json.get_data()
        return self.__convert_json_to_xml(data)

    def __convert_json_to_xml(self, json: JSON) -> XML:

        # Conversion logic
        return XML()


class InheritanceJSONToXMLAdapter(AbstractClientXMLParser, ServiceJSON):

    def process_data(self) -> XML:
        data = self.get_data()
        return self.__convert_json_to_xml(data)

    def __convert_json_to_xml(self, json: JSON) -> XML:

        # Conversion logic
        return XML()

# Notes

# When to use
# Adapt a class whose' interface is not compatible with the rest of the code

# How to implement
# 1. Declare Client interface (AbstractClientXMLParser) and create abstract method for communication
# with service (process_data)
# 2. Create ConcreteAdapter and make it follow interface (CompositionJSONToXMLAdapter, InheritanceJSONToXMLAdapter)
# 3. Implement abstract method in ConcreteAdapter, either calling to composed Service or inheriting Service (ServiceJSON)
