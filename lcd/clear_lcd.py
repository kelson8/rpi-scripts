# Clear the lcd screen

from LCD1602 import CharLCD1602

lcd = CharLCD1602()

def clear_lcd():
    lcd.clear()

if __name__ == '__main__':
    clear_lcd()
