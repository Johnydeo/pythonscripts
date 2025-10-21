#!/usr/bin/env python3
import os
import time
import sys
import random

LED_NAME = "input0::capslock"
LED_PATH = f"/sys/class/leds/{LED_NAME}/brightness"


def checkleds():
    if not os.path.exists(LED_PATH):
        print("Error LED doesnot exists ")
        print(
            "Avialable_leds",
            os.listdir(LED_PATH.replace(f"/{LED_NAME}/brightness", "")),
        )
        sys.exit()


def set_brightness(value):
    try:
        with open(LED_PATH, "w") as file:
            file.write(value)
    except Exception as e:
        print(f"Error writitng to led {e}")
        sys.exit(0)


def main():
    checkleds()
    try:
        while True:
            set_brightness(str(255))
            time.sleep(random.randint(1, 4))
            set_brightness(str(0))
            time.sleep(random.randint(1, 3))

    except KeyboardInterrupt:
        print("Stopping .. turning LED off")
        set_brightness(str(0))
        sys.exit(0)


if __name__ == "__main__":
    main()
