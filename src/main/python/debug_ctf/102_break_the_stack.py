# The goal is to force the returns_false() function to return True, so that the assert pass. So, no jumping.
# I don't know how to do it, or if it's possible (surely it is) :sadpanda:
def returns_false():
    breakpoint()
    return False

assert(returns_false())
print("Flag captured")
