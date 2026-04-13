from machine import Pin
import time

# ----- Keypad Row Pins -----
rows = [Pin(0, Pin.OUT), Pin(1, Pin.OUT),
        Pin(2, Pin.OUT), Pin(3, Pin.OUT)]

# ----- Keypad Column Pins -----
cols = [Pin(4, Pin.IN, Pin.PULL_DOWN),
        Pin(5, Pin.IN, Pin.PULL_DOWN),
        Pin(6, Pin.IN, Pin.PULL_DOWN),
        Pin(7, Pin.IN, Pin.PULL_DOWN)]

# ----- Relay and Buzzer -----
relay = Pin(8, Pin.OUT)
buzzer = Pin(9, Pin.OUT)

# ----- Keypad Layout -----
keys = [
    ['1','2','3','A'],
    ['4','5','6','B'],
    ['7','8','9','C'],
    ['*','0','#','D']
]

# ----- Set Password -----
correct_password = "1234"
entered_password = ""

print("Door Lock System Ready")

while True:
    for i in range(4):

        # Set all rows LOW
        for r in rows:
            r.value(0)

        # Set current row HIGH
        rows[i].value(1)

        for j in range(4):
            if cols[j].value() == 1:

                key = keys[i][j]
                print("Pressed:", key)

                # If digit pressed
                if key.isdigit():
                    entered_password += key
                    print("Entered:", entered_password)

                # If # pressed → Check password
                elif key == '#':
                    if entered_password == correct_password:
                        print("Access Granted")
                        relay.value(1)  # Unlock
                        time.sleep(5)   # Door open for 5 sec
                        relay.value(0)  # Lock again
                    else:
                        print("Access Denied")
                        buzzer.value(1)
                        time.sleep(2)
                        buzzer.value(0)

                    entered_password = ""  # Reset

                # If * pressed → Clear
                elif key == '*':
                    entered_password = ""
                    print("Cleared")

                # Wait until key release
                while cols[j].value() == 1:
                    pass
                time.sleep(0.3)