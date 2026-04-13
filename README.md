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

