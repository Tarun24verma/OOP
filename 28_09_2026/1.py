import time
from functools import wraps 

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timer] {func.__name__} took {elapsed:.6f}s")
        return result
    return wrapper

def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrappper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrappper
    return decorator

@timer
@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
    return name.upper()

@repeat(2)
@timer
def compute(x):
    return sum(i*i for i in range(x))

if __name__ == "__main__":
    greet("mona")
    compute(100_00)
