"""Module contains a simple Proxy"""
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Data:
    id_: int


class DatabaseRetriever(ABC):

    @abstractmethod
    def retrieve_data(self, id_: int) -> Data:
        pass


class DatabaseService(DatabaseRetriever):
    def retrieve_data(self, id_: int) -> Data:
        # Expensive request
        return Data(id_)


class Proxy(DatabaseRetriever):
    def __init__(self, database_service: DatabaseService) -> None:
        self.database_service = database_service
        self.__cache = {}

    def retrieve_data(self, id_: int) -> Data:
        if self.__cache(id_) is not None:
            return self.__cache(id_)
        data = self.database_service.retrieve_data(id_)
        self.__cache[id_] = data
        return data
# Notes

# When to use
# When calls to service are expensive or restrictive

# How to implement
# 1. Create an AbstractServiceOperator (DatabaseRetriever)
# 2. Create Proxy that implements AbstractServiceOperator and that is composed of ExpensiveService (DatabaseService)
# 3. Client handle requests with Proxy to retrieve ExpensiveService method
