# Smart Light - Wi-Fi Controlled LED

Control an LED connected to a Raspberry Pi over Wi-Fi from your smartphone or laptop.

---

## 🔹 Project Overview

This project demonstrates a simple IoT-style smart light system using a Raspberry Pi. A web interface allows you to **turn an LED ON, OFF, or make it BLINK** remotely. The Raspberry Pi can be accessed both **locally** over your Wi-Fi network and **remotely** using [Remote.It](https://remote.it/).

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

## 🧩 Wiring

1. Connect the **long leg (anode)** of the LED to a GPIO pin on Raspberry Pi (example: GPIO 17).  
2. Connect the **short leg (cathode)** of the LED to one end of a 150Ω resistor.  
3. Connect the other end of the resistor to a **GND pin** on the Raspberry Pi. 


> ⚠️ Always check LED polarity: anode = positive, cathode = negative.

---

## 🛠️ Software Setup

### 1. Raspberry Pi OS Setup

1. Flash Raspberry Pi OS onto SD card.  
2. Enable SSH: create an empty file named `ssh` in the boot partition.  
3. Configure Wi-Fi by editing `wpa_supplicant.conf` in the boot partition:
   ```text
   country=BA
   ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
   update_config=1

   network={
       ssid="###"
       psk="#########"
   }


4. Insert SD card, power on Raspberry Pi, and find its IP on your network (`nmap` or router admin page).

---

### 2. Remote Access (Optional)

We used **Remote.It** to allow remote access outside your local network:

1. Create a Remote.It account at [https://app.remote.it](https://app.remote.it).
2. Install Remote.It agent on the Pi:

   ```bash
   curl -L https://downloads.remote.it/remoteit/install_agent.sh | sh
   ```
3. Register the Pi in your account.
4. Add services: **SSH (port 22)** and **HTTP (port 80)**.
5. Remote.It provides a hostname and port to connect from anywhere.

---

### 3. Install Required Software

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install apache2 php libapache2-mod-php python3-rpi.gpio git -y
```

#### 🤔 Technologies for achieving the project goals are under consideration and will be finalized during planning.

---

## 🔗 Git Integration

* Clone the repository to your Pi or local machine:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

* Pull latest updates:

```bash
git pull origin main
```

* Commit changes:

```bash
git add .
git commit -m "Your message"
git push origin main
```

> This allows team collaboration and distributing the project to multiple Raspberry Pis.

---

## ✅ What’s Implemented

* Headless Raspberry Pi setup with Wi-Fi and SSH.
* Remote access via Remote.It.
* Apache + PHP web server.
* Git integration for project version control.

---

## 🌟 Future Improvements / Ideas

* Add multiple LEDs or RGB LEDs and allow color control.
* Add authentication to the web interface for security.
* Implement smartphone app instead of PHP webpage.
* Add scheduling (turn on/off at specific times).
* Use WebSocket for real-time LED status updates.
* Add MQTT support to integrate with home automation platforms.

---

## 📄 References

* [RPi.GPIO Python library](https://pypi.org/project/RPi.GPIO/)
* [Remote.It Documentation](https://docs.remote.it/)
* [Raspberry Pi OS Setup Guide](https://www.raspberrypi.com/software/)

---

## 👥 Authors
- **Riad Elezovic**  
- **Kerim Kapetanovic**  
- **Amar Dizdarevic**  
- **Mustafa Sinanovic**  

## 📅 Project Start Date
**5 November 2025**

