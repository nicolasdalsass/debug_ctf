import numpy as np

def get_random_int():
    return np.random.randint(1, 100)

def get_random_float():
    return np.random.random()

get_random_int()
get_random_float()

# IntelliJ : You're only allowed to breakpoint on the print() line
# VSCode : you're allowed to breakpoint where you want, but you're not allowed to change any state whatsoever
print("The flag is captured if you know the returned values of the two functions.")
