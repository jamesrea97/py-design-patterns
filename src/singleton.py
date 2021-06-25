"""Module contains a simple Singleton Design Pattern"""
import random


class Database:

    def __init__(self):
        self.data = random.random()

    def get_data(self) -> str:
        return "Data: " + str(self.data)


class DatabaseSingleton:
    """
    Singleton Product class
    Role: Creates only one instance
    """

    def __init__(self) -> None:
        self.__database = None

    def get_instance(self) -> Database:

        if self.__database is None:
            self.__database = Database()
        return self.__database


# Notes

# When to use
# Want a single instance to all users

# How to implement:
# 1. Create a Singleton and Singletee classs
# 2. Create a get_instance method in Singleton that produces only one instance of the Singletee class
