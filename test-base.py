from datetime import datetime
import RPi.GPIO as GPIO
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
import logging
logging.basicConfig(level=logging.INFO)

# インターバル
INTERVAL = 3
# スリープタイム
SLEEPTIME = 20
# 使用するGPIO
GPIO_PIN = 18
# video url
VIDEO_PATH = Path("../tests/media/test_media_1.mp4")

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

player.playEvent += lambda _: player_log.info("Play")
player.pauseEvent += lambda _: player_log.info("Pause")
player.stopEvent += lambda _: player_log.info("Stop")

if __name__ == '__main__':
    try:
        print ("start niwa")
        while True:
            # センサー感知
            print("video start")
            if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
                player = OMXPlayer(VIDEO_PATH)
                player.play()
                player.stop()

            else:
                player.pause()
                # time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("終了処理中...")
    finally:
        GPIO.cleanup()
        print("GPIO clean完了")
