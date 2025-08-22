# exercise5.py - Countdown with Early Exit

import time

secs_str = input("Enter seconds: ").strip()
if secs_str.isdigit():
    secs = int(secs_str)
    if secs > 10:
        print("Too long! Try a smaller number.")
    else:
        while secs > 0:
            print(secs)
            time.sleep(1)   # optional delay for realism
            secs -= 1
        print("Liftoff!")
else:
    print("Please enter a positive integer.")
