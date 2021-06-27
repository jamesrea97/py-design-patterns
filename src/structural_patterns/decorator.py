"""Module contains Decorator Design Pattern"""
from typing import Callable


# Python in-built decorator

def get_pass_failed(get_score: Callable):
    def wrapper(bonus: int = None):
        score = get_score()
        score += bonus if bonus is not None else 0
        if score > 40:
            return "Passed"
        else:
            return "Failed"
    return wrapper


@get_pass_failed
def get_score_implementation():
    return 30
