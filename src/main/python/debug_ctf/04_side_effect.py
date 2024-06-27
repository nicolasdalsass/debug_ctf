import numpy as np

a = np.random.random_integers(100, size=100)

def printer(i: int):
    print(i)  # This is the only line where you're allowed to put a breakpoint !

for i in a:
    printer(i)

try:
    with open("test.txt", "r") as f:
        b = f.readlines()
        for i in range(len(a)):
            assert a[i] == int(b[i])
        print("Flag captured")
finally:
    import os

    if os.path.exists("test.txt"):
        os.remove("test.txt")
