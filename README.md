# Notes

## A note on abstractmethod
```py
from abc import ABC, @abstractmethod 

class NonAbstractObject:

    @abstractmethod 
    def function():
        pass

class AbstractObject(ABC):

    @abstractmethod 
    def function():
        pass

# NonAbstractObject is not abstract... @abstractmethod only changes the __isabstractmethod__ = True
# AbstractObject is abstract

NonAbstractObject() # valid
NonAbstractObject().function() # invalid as not implemented
AbstractObject() # invalid as abstract

```