# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
from Wifi import connect_to_wifi
from config import config


connect_to_wifi(config['network']['ssid'], config['network']['password'])