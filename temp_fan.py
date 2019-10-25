# 温控风扇V2.1

import RPi.GPIO as GPIO
from configparser import ConfigParser
import sys
import time

GPIO.setmode(GPIO.BOARD)
pin = 12
config = ConfigParser()

GPIO.setup(pin, GPIO.OUT)


def fan_start():
    GPIO.output(pin, True)


def fan_stop():
    GPIO.output(pin, False)


while True:
    file = open('/sys/class/thermal/thermal_zone0/temp')
    temp = (int)(file.read())
    file.close()
    
    config_path = '/home/pi/workplace/utils/temp_fan/fan.conf'
    config.read(config_path)

    if config.getboolean('force', 'disabled'):
        # config.clear()
        time.sleep(config.getint('settings', 'sleep_time'))
        continue
    
    # print(temp)
    # 高温且风扇未开
    if temp > config.getint('settings', 'high_temp') and not config.getboolean('fan_status', 'fan_status'):
        fan_start()
        # print('open')
        # fan_status = False
        config.set('fan_status', 'fan_status', 'True')
    # 低温且风扇开了
    elif temp < config.getint('settings', 'low_temp') and config.getboolean('fan_status', 'fan_status'):
        fan_stop()
        # print('close')
        # fan_status = False
        config.set('fan_status', 'fan_status', 'False')
    config.write(open(config_path, 'w'))
    # config.clear()
    # 延时
    time.sleep(config.getint('settings', 'sleep_time'))
