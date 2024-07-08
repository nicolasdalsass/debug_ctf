import numpy as np

def get_random_int():
    return np.random.randint(1, 100)

def get_random_float():
    return np.random.random()

get_random_int()
get_random_float()

print("The flag is captured if you know the returned values of the two functions.") # You're only allowed to breakpoint here
