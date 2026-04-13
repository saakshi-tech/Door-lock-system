# Door-lock-system
# 🔐 Door Lock System using Keypad (MicroPython)

## 📌 Overview
This project is a simple and practical door lock system built using a 4x4 keypad, relay, and buzzer. It runs on a microcontroller using MicroPython.

The idea is straightforward — enter the correct password to unlock the door. If the password is wrong, the system alerts you using a buzzer.

It’s a great beginner-friendly embedded systems project and can be extended into a smart security system.

---

## 🚀 What this system can do
- Lets you unlock a door using a password
- Detects keypad inputs in real time
- Controls a relay to simulate a door lock
- Gives a buzzer alert for wrong attempts
- Allows clearing input using `*`
- Uses `#` to submit the password

---

## 🛠️ Components required
- Microcontroller (ESP32 / Raspberry Pi Pico or similar)
- 4x4 Matrix Keypad
- Relay Module
- Buzzer
- Jumper wires

---

## ⚙️ Pin connections

| Component        | Pins Used |
|----------------|----------|
| Keypad Rows     | 0, 1, 2, 3 |
| Keypad Columns  | 4, 5, 6, 7 |
| Relay           | 8 |
| Buzzer          | 9 |

---

## 🔑 Password info
- Default password: **1234**
- Press `#` to check the password
- Press `*` to clear what you've entered

---

## 🧠 How it works
The system keeps scanning the keypad continuously.

- When you press a number, it gets added to the entered password.
- When you press `#`, the system checks:
  - If the password is correct → the relay turns ON (door unlocks for 5 seconds)
  - If the password is wrong → the buzzer turns ON (alert for 2 seconds)
- Press `*` anytime to reset your input.

---

## 💻 Code

```python
from machine import Pin
import time

rows = [Pin(0, Pin.OUT), Pin(1, Pin.OUT),
        Pin(2, Pin.OUT), Pin(3, Pin.OUT)]

cols = [Pin(4, Pin.IN, Pin.PULL_DOWN),
        Pin(5, Pin.IN, Pin.PULL_DOWN),
        Pin(6, Pin.IN, Pin.PULL_DOWN),
        Pin(7, Pin.IN, Pin.PULL_DOWN)]

relay = Pin(8, Pin.OUT)
buzzer = Pin(9, Pin.OUT)

keys = [
    ['1','2','3','A'],
    ['4','5','6','B'],
    ['7','8','9','C'],
    ['*','0','#','D']
]

correct_password = "1234"
entered_password = ""

print("Door Lock System Ready")

while True:
    for i in range(4):
        for r in rows:
            r.value(0)
        rows[i].value(1)

        for j in range(4):
            if cols[j].value() == 1:
                key = keys[i][j]
                print("Pressed:", key)

                if key.isdigit():
                    entered_password += key
                    print("Entered:", entered_password)

                elif key == '#':
                    if entered_password == correct_password:
                        print("Access Granted")
                        relay.value(1)
                        time.sleep(5)
                        relay.value(0)
                    else:
                        print("Access Denied")
                        buzzer.value(1)
                        time.sleep(2)
                        buzzer.value(0)

                    entered_password = ""

                elif key == '*':
                    entered_password = ""
                    print("Cleared")

                while cols[j].value() == 1:
                    pass
                time.sleep(0.3)
