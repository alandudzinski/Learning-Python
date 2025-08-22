import time

secs_str = input("Enter seconds: ").strip()
if secs_str.isdigit():
    secs = int(secs_str)
    while secs > 0:
        print(secs)
        time.sleep(1)   # optional delay for realism
        secs -= 1
    print("Liftoff!")
else:
    print("Please enter a positive integer.")
