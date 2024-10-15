import os
import sys
import platform

# https://note.nkmk.me/en/python-platform-system-release-version/

#print ("OS: " + os.name)

def print_details():
    # Linux
    if os.name == "posix":
        print("System: " + platform.system())
        # print ("Sys platform: " + sys.platform)
        print("Linux Kernel: " + platform.release())
        print("Platform version: " + platform.version())
        print("Kernel full details: " + platform.platform())
    # Windows
    elif os.name == "nt":
        print("System: " + platform.system())
        # print ("Sys platform: " + sys.platform)
        print("Windows Version: " + platform.release())
        print("Platform version: " + platform.version())
        print("Kernel full details: " + platform.platform())
    # Mac, untested possibly test in a vm sometime.
    elif os.name == "darwin":
        print("System: " + platform.system())
        # print ("Sys platform: " + sys.platform)
        print("Mac Version: " + platform.release())
        print("Platform version: " + platform.version())
        print("Kernel full details: " + platform.platform())

if __name__ == '__main__':
    print_details()

