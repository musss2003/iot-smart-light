# /var/www/html/blink.py
import lgpio
import time
import os
 
LED_PIN = 17
PID_FILE = "/tmp/blink_led.pid"
 
# Save PID of this process
with open(PID_FILE, "w") as f:
    f.write(str(os.getpid()))
 
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, LED_PIN)
 
try:
    while True:
        lgpio.gpio_write(h, LED_PIN, 1)
        time.sleep(0.5)
        lgpio.gpio_write(h, LED_PIN, 0)
        time.sleep(0.5)
finally:
    lgpio.gpiochip_close(h)
    if os.path.exists(PID_FILE):
        os.remove(PID_FILE)