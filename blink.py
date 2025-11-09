import lgpio
import time

LED_PIN = 17
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, LED_PIN)

try:
    while True:
        lgpio.gpio_write(h, LED_PIN, 1)
        time.sleep(0.5)
        lgpio.gpio_write(h, LED_PIN, 0)
        time.sleep(0.5)
except KeyboardInterrupt:
    lgpio.gpiochip_close(h)
