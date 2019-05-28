from datetime import datetime
import RPi.GPIO as GPIO
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

# インターバル
INTERVAL = 3
# スリープタイム
SLEEPTIME = 20
# 使用するGPIO
GPIO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

if __name__ == '__main__':
    try:
        print ("処理キャンセル：CTRL+C")
        cnt = 1
        while True:
            # センサー感知
            if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
                VIDEO_PATH = Path("../tests/media/test_media_1.mp4")
                player = OMXPlayer(VIDEO_PATH)
                sleep(5)
            else:
                print(GPIO.input(GPIO_PIN)) 
                time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("終了処理中...")
    finally:
        GPIO.cleanup()
        print("GPIO clean完了")