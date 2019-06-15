# coding: utf-8
# from omxplayer.player import OMXPlayer
#from pathlib import Path
from smbus2 import SMBus
import time

# VIDEO_PATH = Path("path")

bus_number = 1
i2c_address = 0x76

bus = SMBus(bus_number)

digT = []

t_fine = 0.0


def writeReg(reg_address, data):
    bus.write_byte_data(i2c_address, reg_address, data)


def get_calib_param():
    calib = []

    for i in range(0x88, 0x88+24):
        calib.append(bus.read_byte_data(i2c_address, i))
    calib.append(bus.read_byte_data(i2c_address, 0xA1))
    for i in range(0xE1, 0xE1+7):
        calib.append(bus.read_byte_data(i2c_address, i))

    digT.append((calib[1] << 8) | calib[0])
    digT.append((calib[3] << 8) | calib[2])
    digT.append((calib[5] << 8) | calib[4])


def readData():
    data = []
    for i in range(0xF7, 0xF7+8):
        data.append(bus.read_byte_data(i2c_address, i))
    temp_raw = (data[3] << 12) | (data[4] << 4) | (data[5] >> 4)

    compensate_T(temp_raw)


def compensate_T(adc_T):
    arrTemp = []
    global t_fine
    v1 = (adc_T / 16384.0 - digT[0] / 1024.0) * digT[1]
    v2 = (adc_T / 131072.0 - digT[0] / 8192.0) * \
        (adc_T / 131072.0 - digT[0] / 8192.0) * digT[2]
    t_fine = v1 + v2
    temperature = t_fine / 5120.0
    print "temp : %-6.2f ℃" % (temperature)
    arrTemp.append(temperature)
    print (arrTemp)


def setup():
    osrs_t = 1  # Temperature oversampling x 1
    mode = 3  # Normal mode
    t_sb = 5  # Tstandby 1000ms
    filter = 0  # Filter off
    spi3w_en = 0  # 3-wire SPI Disable

    ctrl_meas_reg = (osrs_t << 5) | mode
    config_reg = (t_sb << 5) | (filter << 2) | spi3w_en

    writeReg(0xF4, ctrl_meas_reg)
    writeReg(0xF5, config_reg)


setup()
get_calib_param()


if __name__ == '__main__':
    try:
        while True:
            readData()
            time.sleep(5)
    except KeyboardInterrupt:
        pass
