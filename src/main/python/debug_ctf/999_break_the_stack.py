# It's extremely stupidly hard, don't lose your sanity ^^'
def returns_false():
    breakpoint()
    return False

assert(returns_false())
print("Hello world")
