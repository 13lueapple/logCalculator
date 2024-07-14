import time

def timer(func, args: list):
    startTime = time.time()
    func(*args)
    endTime = time.time()
    return endTime - startTime