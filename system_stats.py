import subprocess
import time
import psutil

# Fix for the bytes showing up in the string:
# https://stackoverflow.com/questions/15374211/why-does-popen-communicate-return-bhi-n-instead-of-hi

# https://raspberrypi.stackexchange.com/questions/111337/temperature-measured-using-psutil-and-the-cpu-temperature-monitor-are-differ
def get_cpu_temp():
    temp_file = open("/sys/class/thermal/thermal_zone0/temp")
    cpu_temp = temp_file.read()
    temp_file.close()
    return round(float(cpu_temp) / 1000, 2)
    # print(cpu.temperature)
    
def get_cpu_usage():
    return psutil.cpu_percent()
    

# https://pypi.org/project/psutil/ 

def print_stats():
    while True:
        cpu_temp = psutil.sensors_temperatures()
        cpu_usage = psutil.cpu_percent()
    
    
        cmd = "hostname -I | cut -d\' \' -f1"
        IP = subprocess.check_output(cmd, shell = True, universal_newlines=True ).strip()
        cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell = True, universal_newlines=True )
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell = True, universal_newlines=True )
        cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
        Disk = subprocess.check_output(cmd, shell = True, universal_newlines=True )

        cmd = "ifstat -i eth0 1 1 | tail -n1"
        NetUsage = subprocess.check_output(cmd, shell = True, universal_newlines = True)

        # print(f"{IP}\n{CPU}%\n{MemUsage}\n{Disk}\n{NetUsage}")
        # print(cpu_temp)
        print(f"{IP}\n{cpu_usage}\n{MemUsage}\n{Disk}\n{NetUsage}")
        time.sleep(1)

# print_stats()
# cpu_temp = psutil.sensors_temperatures()
cpu_temp = get_cpu_temp()
# print(cpu_temp)
print(f"{cpu_temp}C")