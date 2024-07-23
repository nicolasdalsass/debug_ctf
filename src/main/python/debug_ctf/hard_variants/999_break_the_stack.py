# It's extremely stupidly hard, don't lose your sanity ^^'
# You're only allowed to breakpoint once the returns_false() method has started to run.
# The hope is to force a function to return something else.
# The general case is unsolved, however in the specific case of a boolean, there's a way to hack it.
def returns_false():
    # # Feel free to add a breakpoint() if you prefer
    return False

assert(returns_false())
print("Hello world")
