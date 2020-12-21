with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
    temp = (int)(f.read())
    print(temp)
