from functools import wraps

import pytest


def print_test_message(message):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"\nDEBUT DU TEST : {message}")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator