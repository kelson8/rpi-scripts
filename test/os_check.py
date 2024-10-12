import os
import sys
import platform

# https://note.nkmk.me/en/python-platform-system-release-version/

#print ("OS: " + os.name)
print ("System: " + platform.system())
#print ("Sys platform: " + sys.platform)
print ("Linux Kernel: " + platform.release())
print ("Platform version: " + platform.version())
print ("Kernel full details: " + platform.platform())
