# 💡 Smart Light – Raspberry Pi IoT Project

## 🧠 Overview
**Smart Light** is an IoT project that demonstrates how to control an LED remotely over Wi-Fi using a **Raspberry Pi**.  
By hosting a simple **web server** on the Raspberry Pi, users can toggle the LED **ON**, **OFF**, or make it **BLINK** directly from any smartphone or computer connected to the same network.

This project integrates **web development (PHP)**, **hardware control (Python + GPIO)**, and **basic networking** concepts.

---

## ⚙️ Features
- 💡 **Turn LED ON** – instantly light up the LED via a web interface  
- 🌑 **Turn LED OFF** – switch off the LED remotely  
- ⚡ **Blink Mode** – continuously blink the LED (0.5 s ON / 0.5 s OFF)  
- 🌐 **Wi-Fi Control** – access the interface from any device on the same network  
- 📡 *(Optional Bonus)*: Raspberry Pi broadcasts its own Wi-Fi hotspot for direct control  

---

## 🧰 Hardware Components
| Component | Description |
|------------|-------------|
| 💡 LED | Standard 5 mm LED (any color) |
| 🔌 150 Ω Resistor | Current-limiting resistor for the LED |
| 🔲 Breadboard | For easy wiring |
| 🔗 Jumper Wires | Female-to-male wires to connect Pi GPIO pins |
| 🍓 Raspberry Pi | Any model with GPIO (e.g., Pi 3 / 4 / Zero W) |
| 📱 Smartphone / Laptop | Device to access the web interface |

---

## 🔌 Wiring Diagram
| Raspberry Pi Pin | Connection | Description |
|------------------|-------------|-------------|
| GPIO 17 (Pin 11) | → LED (+) | LED positive leg (anode) |
| GND (Pin 6) | → LED (–) via 150 Ω resistor | LED ground through resistor (cathode) |

> 💡 **Note:**  
> The long leg of the LED is **positive (+)**.  
> Always use a **resistor** to avoid burning the LED or damaging your GPIO.

---
