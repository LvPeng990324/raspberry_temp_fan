# raspberry_temp_fan
可以根据CPU温度控制树莓派散热风扇开关的脚本


# 支持配置文件热拔插
当你修改配置文件时，只要保存，程序会自动检测更改并重新载入配置信息


# 风扇安装方法
正极插树莓派5V输出针，如果是三线的（自带信号端），信号线插板子的12号PIN（就是上数第六行右边那个），负极插接地针；如果跟我一样，只有双线，不自带信号端的辣鸡风扇，可以搞一个开关三极管，然后负极插三极管的正极针（VCC），三极管的接地针（GND）插树莓派的接地针，三极管剩下的那个VIN针插板子的12号PIN，然后就可以了。


# 脚本使用方法
下载配置文件和脚本文件并放在同一目录下

在该目录打开终端，执行python3 temp_fan.py &

可以在/etc/rc.local文件中添加该命令来设置开机自启动，注意路径要写成绝对路径～

enjoy it!


# 配置文件自定义方法
文本编辑器打开配置文件，然后直接修改你想修改的值就可以了，保存后脚本会自动重新加载。

[settings]中是对温度阈值的设置以及状态更新频率的设置，温度除以1000就是摄氏度；sleep_time是更新频率，即多少秒检查一次温度并决定是否更新风扇状态。

[fan_status]中的fan_status是记录当前风扇的状态的，由程序自行写入，请不要修改！

[force]中的disabled是手动控制，默认为False，如果设置为True，那么将不会对风扇进行控制，会一直维持当前状态。
