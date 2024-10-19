import io
import os

# https://raspberrypi.stackexchange.com/questions/5100/detect-that-a-python-program-is-running-on-the-pi

def is_raspberrypi():
    try:
        with io.open('/sys/firmware/devicetree/base/model', 'r') as m:
            if 'raspberry pi' in m.read().lower():
                return True
    except FileNotFoundError:
        pass
       #return
       #print("File not found!")
    return False

def main():
    if is_raspberrypi():
        print("You are running a raspberry pi")
    else:
        print("You are not running a raspberry pi")

# if __name__ == '__main__':
#     main()