import RPi.GPIO as GPIO
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

# 使用するGPIO
GPIO_PIN = 18
# video url
VIDEO_PATH = Path("path")
VIDEO_PATH_SUB = Path("path_sub")

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

sleep(3)
player_sub = OMXPlayer(VIDEO_PATH_SUB)

sleep(3)
player_sub.set_position(0)
player_sub.pause()

if __name__ == '__main__':
    try:
        print ("start niwa")
        while True:
            if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
                print("true")
                player = OMXPlayer(VIDEO_PATH)
                sleep(3)
            else:
                print("no signal")
                sleep(3)
    except KeyboardInterrupt:
        print("終了処理中...")
    finally:
        GPIO.cleanup()
        print("GPIO clean完了")
