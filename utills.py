import time

def time_it(func): # example of decorator.
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start) * 1000} ms to execute.")
        return result
    return wrapper