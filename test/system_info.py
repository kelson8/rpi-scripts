import psutil

import math
from time import sleep
import os

# Using this for converting file sizes:
# https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

# Most of this came from the docs here:
# https://psutil.readthedocs.io/en/latest/

# Mostly created in nano on Linux

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

mem = psutil.virtual_memory()

def main():
#    print("             Ram info:")
    while True:
        print("             Ram info:")
        # Pad the text a bit with some spacing
        print("")
        print(f"Total RAM: {convert_size(mem.total)}")
        print(f"Available RAM: {convert_size(mem.available)}")
        print(f"Percent Used: {mem.percent}%")
        print(f"Used RAM {convert_size(mem.used)}")
        print(f"Free RAM {convert_size(mem.free)}")

        print("")
        print("              Cpu info:")

        sleep(1)
        os.system("clear")


def cpu_freq():
    cpu_usage = psutil.cpu_freq()
    print("Cpu usage: ")
    # Give the usage in ghz instead of mhz
    print(f"Cpu frequency Ghz: {cpu_usage.current / 1000 }Ghz")
    print(f"Cpu frequency Mhz: {cpu_usage.current }Mhz")
    # Not needed for the loop
    #print(f"Current: {cpu_usage.current}")
    #print(f"Min: {cpu_usage.min}")
    #print(f"Max: {cpu_usage.max}")

def print_cpu_freq():
    while True:
        cpu_freq
        sleep(1)
        os.system("clear")

def disks():
    print("\nDisk usage: ")
    print(f"Total Disk space: {convert_size(psutil.disk_usage('/').total)}")
    print(f"Disk usage: {convert_size(psutil.disk_usage('/').used)}")
    # This is a bit spammy.
#    print(f"Partitions: {psutil.disk_partitions()}")

def print_disks():
    while True:
        disks()
        sleep(1)
        os.system("clear")

def network():
    netusage = psutil.net_io_counters()
    print("\nNetwork usage: ")
    print(f"Bytes sent: {convert_size(netusage.bytes_sent)}")
    print(f"Bytes received: {convert_size(netusage.bytes_recv)}")

def print_network():
    while True:
        network()
        sleep(1)
        os.system("clear")

# Changed this to use the format below, now each of these can be toggled.
def print_all():
    cpu_freq_enabled = True
    disks_enabled = True
    network_enabled = True
    
    while True:
        if cpu_freq_enabled:
            cpu_freq()
        if disks_enabled:
            disks()
        if network_enabled:
            network()
        sleep(1)
        os.system("clear")
        



if __name__ == '__main__':
    try:
#        main()
        #cpu_freq()
        print_all()
    except KeyboardInterrupt:
        exit()
