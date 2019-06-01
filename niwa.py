import RPi.GPIO as GPIO
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep


# using GPIO
GPIO_PIN = 18
# video url
VIDEO_PATH = Path("Path")

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)


if __name__ == '__main__':
    try:
        print ("start niwa")
        while True:
            if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
                print("found a human")
                player = OMXPlayer(VIDEO_PATH)
                sleep(5)
            else:
                print("no signal")
                sleep(5)
    except KeyboardInterrupt:
        print("interrupted")
    finally:
        GPIO.cleanup()
        print("GPIO clean")
