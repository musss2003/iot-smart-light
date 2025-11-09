# /var/www/html/turnon.py
import lgpio
import os
import signal
 
LED_PIN = 17
PID_FILE = "/tmp/blink_led.pid"
 
# Kill blinking if running
if os.path.exists(PID_FILE):
    with open(PID_FILE, "r") as f:
        pid = int(f.read())
    os.kill(pid, signal.SIGTERM)
    os.remove(PID_FILE)
 
# Turn LED ON
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, LED_PIN)
lgpio.gpio_write(h, LED_PIN, 1)
lgpio.gpiochip_close(h)