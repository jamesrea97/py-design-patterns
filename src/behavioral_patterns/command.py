from abc import abstractmethod


"""Module contains a simple Command Design Pattern"""
from abc import ABC, abstractmethod


class AbstractLongTask(ABC):
    @abstractmethod
    def run(self) -> str:
        pass


class LongTaskA(AbstractLongTask):
    def step_one(self) -> str:
        return "LongTaskA Step 1 Completed"

    def step_two(self) -> str:
        return "LongTaskA Step 2 Completed"

    def run(self) -> str:
        return ",".join((self.step_one(), self.step_two()))


class LongTaskB(AbstractLongTask):
    def task_one(self) -> str:
        return "LongTaskB Step 1 Completed"

    def task_two(self) -> str:
        return "LongTaskB Step 2 Completed"

    def run(self) -> str:
        return ",".join((self.task_one(), self.task_two()))


class Executer:
    def execute(self, task: AbstractLongTask) -> str:
        return task.run()

# When to use
# When you would like to execute a long task that can take many forms

# How to create
# 1. Create a AbtractTask that has abstractmethod run
# 2. For each task, implement run as desired
# 3. Create an execute method that takes AbtractTask as a parameter and pass it the concrete task,
# in execute method call run from AbstractTask.
