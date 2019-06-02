from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

VIDEO_PATH = Path("your path")

sleep(3)
player = OMXPlayer(VIDEO_PATH)

sleep(3)
player.set_position(0)
player.pause()

sleep(5)
