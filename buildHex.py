import subprocess
import os
import sys

path = "build"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

os.chdir(path)

cmd = ["cmake", "../examples/blinky"]

retVal = subprocess.call(cmd)

if(retVal == 0):
    cmd = ["cmake", "--build", ".", "--target", "blinky.hex"]
    retVal = subprocess.call(cmd)
else:
    print ("CMake cache generation failed")

sys.exit(retVal)
