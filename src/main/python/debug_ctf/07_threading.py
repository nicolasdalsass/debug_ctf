import concurrent.futures
import time


def threaded_function():
    print("Frames not available in non-suspended state ?")  # You're only allowed to breakpoint here


def evil_threaded_function():
    c = False
    time.sleep(1)
    return c


with concurrent.futures.ThreadPoolExecutor() as executor:
    a = executor.submit(evil_threaded_function)
    executor.submit(threaded_function)
    assert (a.result())
    print("Flag captured")
