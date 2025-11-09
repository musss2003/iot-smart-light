import lgpio
import time

# Define LED pin (GPIO17 for example)
LED_PIN = 17

# Open GPIO chip
h = lgpio.gpiochip_open(0)

# Set LED pin as output
lgpio.gpio_claim_output(h, LED_PIN)

# Turn LED ON
lgpio.gpio_write(h, LED_PIN, 1)

# Keep it on for 2 seconds (optional)
time.sleep(2)

# Close chip
lgpio.gpiochip_close(h)
