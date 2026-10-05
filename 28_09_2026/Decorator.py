def timer(func):
    import time
    def wrapper(*args, **kwargs):
        starttime=time.time()
        result=func(*args, **kwargs)
        endtime=time.time()
        print(f"function {func.__name__}: {endtime - starttime} seconds")
        return result
    return wrapper
def test():
    import time
    time.sleep(1)
    print("test function executed")

test = timer(test)
test()