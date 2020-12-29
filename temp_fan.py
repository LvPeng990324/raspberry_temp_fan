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


# 从命令行参数获取配置文件路径
# 判断参数列表长度，看是否提供了配置文件目录
argv_list = sys.argv
if len(argv_list) != 2:
    # 如果参数列表长度不是2，表明给的参数不止一个或没给参数，报错提示并退出
    raise '参数长度不正确，请给出仅一个配置文件路径参数，如果路径含有空格请使用单/双引号包裹'
# 取出配置文件路径
config_path = argv_list[1]

while True:
    file = open('/sys/class/thermal/thermal_zone0/temp')
    temp = (int)(file.read())
    file.close()
    
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
