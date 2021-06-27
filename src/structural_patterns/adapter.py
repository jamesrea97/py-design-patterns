"""Module contains a simple Adapter"""


from typing import Collection


class XML:
    """Contains XML Example"""


class JSON:
    """Contains JSON Example"""


class ClientXMLParser:
    def process_data(self) -> XML:
        return JSONToXMLAdapter().get_data()


class ServiceJSON:
    def get_data(self) -> JSON:
        return JSON()


class JSONToXMLAdapter:
    def __init__(self) -> None:
        self.client_json = ServiceJSON()

    def get_data(self) -> XML:
        json = self.client_json.get_data()

    def __convert_json_to_xml(self, json: JSON) -> XML:

        # Conversion logic
        return XML()
