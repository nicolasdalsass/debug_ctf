class Evil:
    def capture_the_flag(self):
        return False

assert(Evil().capture_the_flag())
print("Flag captured")