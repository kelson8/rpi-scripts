from gpiozero.pins.native import NativeFactory

# This prints out a list of the pins on the gpio with board numbers

factory = NativeFactory()
j8 = factory.board_info.headers['J8']
#print(f'{j8}')
print(f'{j8:full}')