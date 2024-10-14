from gpiozero import LED

green_led = LED(16)
yellow_led = LED(20)
red_led = LED(21)

green_led.off()
yellow_led.off()
red_led.off()