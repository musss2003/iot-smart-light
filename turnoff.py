import lgpio

LED_PIN = 17
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, LED_PIN)
lgpio.gpio_write(h, LED_PIN, 0)
lgpio.gpiochip_close(h)
