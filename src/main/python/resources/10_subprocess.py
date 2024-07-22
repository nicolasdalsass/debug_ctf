# Feel free to change this block to accomodate your own tooling
# Do not however run this file, this is a resource file !

#pycharm variant
import pydevd_pycharm
pydevd_pycharm.settrace('localhost', port=34165, stdoutToServer=True, stderrToServer=True, suspend=True)

# debupgy variant
# import debugpy
# debugpy.listen(34165)
# debugpy.wait_for_client()
###############################################################
a = False
assert(a)
print("Flag captured")