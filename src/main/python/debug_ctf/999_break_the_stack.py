# It's extremely stupidly hard, don't lose your sanity ^^'
def returns_false():
    breakpoint() # Feel free to remove this if you prefer to use another debugger (but you're only allowed to breakpoint on line 4 then.
    return False

assert(returns_false())
print("Hello world")
