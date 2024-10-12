# Show the cpu temp, percent used, ram in use/free, network activity download and upload.
from time import sleep
import os
import psutil

import math
# Using this for converting file sizes:
# https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

# Temperature in Celsius
def get_cpu_temp():
    # Get CPU temperature from file "/sys/class/thermal/thermal_zone0/temp"
    if os.name == "posix":
        tmp = open('/sys/class/thermal/thermal_zone0/temp')
        cpu = tmp.read()
        tmp.close()
        return '{:.2f}'.format( float(cpu)/1000 )

def main():
    while True:
        print(f"Cpu temperature: {get_cpu_temp()} C")
        print(f"Cpu usage: {psutil.cpu_percent()}%")
        print("Ram usage: ")
        print(f"Ram: {psutil.virtual_memory()}")
        sleep(1)
        os.system("clear")


def exit_program():
    # Clear the terminal and exit.
#    os.system("clear")
    exit()


if __name__ == '__main__':
   try:
      main()
   except KeyboardInterrupt:
      exit_program()
