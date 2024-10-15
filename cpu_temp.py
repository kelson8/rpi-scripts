from time import sleep
import os

# Temperature in Celsius
def get_cpu_temp():


    # get CPU temperature from file "/sys/class/thermal/thermal_zone0/temp"
    # Either linux or posix
    if os.name == "posix":
        tmp = open('/sys/class/thermal/thermal_zone0/temp')
        cpu = tmp.read()
        tmp.close()
        return '{:.2f}'.format( float(cpu)/1000 )

    #elif os.name == "nt":
    #    return "ss"

    #elif os.name == "darwin":
    #    return "s"

    # This probably shouldn't be hit if I have all operating systems covered.
    else:
        return "Operating system not setup"


#cpu_temp = get_cpu_temp()

def main():
    # cpu_temp_num = float(cpu_temp)

    # Either linux or posix
   # if os.name == "posix":
     while True:
         print(get_cpu_temp() + ' C')
         sleep(1)

#    elif os.name == "nt":
        # while True:
 #           print("Not implemented")
            # sleep(1)
  #  elif os.name == "darwin":
        # while True:
   #         print("Not implemented")
            # sleep(1)
        
        
        
# Check if the system is running on linux, if not error out.
# I'm not sure how to get cpu temps on Windows in Python.
if __name__ == '__main__':
    try:
        if os.name == "posix" or os.name == "darwin":
            main()
        else:
            print("Operating system not setup")

    except KeyboardInterrupt:
        if os.name == "linux" or os.name == "darwin":
            os.exit()

